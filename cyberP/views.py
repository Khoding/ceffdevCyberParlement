from django.http import JsonResponse, request
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .models import Cyberparlement, Membrecp, Personne, ROLE_MEMBER_KEY, ROLE_CYBERCHANCELIER_KEY, \
    STATUS_POSTED_KEY, STATUS_DRAFT_KEY, VISIBILITY_PUBLIC_KEY, VISIBILITY_PRIVATE_KEY, VISIBILITY_PUBLIC_VALUE, VISIBILITY_PRIVATE_VALUE
from .forms import CyberparlementChangeForm, CyberparlementCreationForm

import json

content = ''
content_move = ''


def get_cyberchancelier_list():
    members = list(Membrecp.objects.values())
    persons = list(Personne.objects.values())
    return [{'person': person,
             'idcyberparlement': member['cyberparlement_id']}
            for person in persons for member in members
            if member['personne_id'] == person['idpersonne']
            and member['rolemembrecyberparlement'] == ROLE_CYBERCHANCELIER_KEY]


def get_cyberparlement_children(tree, id_cyberparlement):
    res = []
    for node in tree:
        if node['cyberparlementparent_id'] == id_cyberparlement:
            res.append(node)
            next_result = get_cyberparlement_children(tree, node['idcyberparlement'])
            if next_result is not None:
                res.extend(next_result)
    return res if res else None


def get_cyberparlement_cyberchancelier(id_cyberparlement):
    if get_cyberchancelier_list() is not None:
        for cyberchancelier in get_cyberchancelier_list():
            if cyberchancelier['idcyberparlement'] == id_cyberparlement:
                return cyberchancelier
    return None


def get_cyberparlement_all_cyberchancelier_list(id_cyberparlement):
    res = [get_cyberparlement_cyberchancelier(id_cyberparlement)]
    cyberparlements = get_cyberparlement_children(list(Cyberparlement.objects.values()), id_cyberparlement)
    if cyberparlements is not None:
        for cyberparlement in cyberparlements:
            res.append(get_cyberparlement_cyberchancelier(cyberparlement['idcyberparlement']))
    return res


def parse_cyberparlement_tree(tree, root, id_cyberparlement_selected):
    res = []
    for child in tree:
        if (root['idcyberparlement'] if root is not None else None) != id_cyberparlement_selected:
            if child['cyberparlementparent_id'] == (root['idcyberparlement'] if root is not None else None):
                child['enfant'] = parse_cyberparlement_tree(tree, child, id_cyberparlement_selected)
                child['allcyberchancelier'] = get_cyberparlement_all_cyberchancelier_list(child['idcyberparlement'])
                res.append(child)
    return res if res else None


def print_cyberparlement_list_tree(tree, id_user):
    global content
    if tree is not None and len(tree) > 0:
        content += '<div class=cp-list-container>'
        for node in tree:
            content += render_to_string(
                'cyberP/cyberparlements/includes/cyberparlement_container_list.html',
                {'cyberparlement': node, 'iduser': id_user},
            )
            print_cyberparlement_list_tree(node['enfant'], id_user)
            content += '</div>'
        content += '</div>'
    return content


def print_cyberparlement_list_move_tree(tree, renderer):
    global content_move
    if tree is not None and len(tree) > 0:
        content_move += '<div class=cp-list-container>'
        for node in tree:
            content_move += render_to_string(
                'cyberP/cyberparlements/includes/cyberparlement_move_container_list.html',
                {'cyberparlement': node}
            )
            print_cyberparlement_list_move_tree(node['enfant'], renderer)
            content_move += '</div>'
        content_move += '</div>'
    return content_move


def get_cyberparlement_list_printed(cyberparlement_list, id_user):
    global content
    content = ''
    cyberchancelier_list = get_cyberchancelier_list()
    for cyberparlement in cyberparlement_list:
        for cyberchancelier in cyberchancelier_list:
            if cyberparlement['idcyberparlement'] == cyberchancelier['idcyberparlement']:
                cyberparlement['cyberchancelier'] = cyberchancelier['person']
    return print_cyberparlement_list_tree(parse_cyberparlement_tree(cyberparlement_list, None, 0), id_user)


def get_cyberparlement_member_list(id_cyberparlement):
    members = list(Membrecp.objects.filter(cyberparlement=id_cyberparlement).values())
    persons = list(Personne.objects.order_by('nom').values())
    cyberparlements = get_cyberparlement_children(list(Cyberparlement.objects.values()), id_cyberparlement)
    if cyberparlements is not None:
        for cyberparlement in cyberparlements:
            cyberparlement_members = list(Membrecp.objects.filter(cyberparlement=cyberparlement['idcyberparlement']).values())
            if cyberparlement_members is not None:
                members.extend(cyberparlement_members)
    persons = [person for person in persons for member in members if member['personne_id'] == person['idpersonne']]
    return [dict(t) for t in {tuple(d.items()) for d in persons if d}]


def get_user_cyberparlement_list(id_user):
    cyberparlements = list(Cyberparlement.objects.order_by('nom').values())
    user_cyberparlement_list = []
    for cyberparlement in cyberparlements:
        for cyberparlement_member in get_cyberparlement_member_list(cyberparlement['idcyberparlement']):
            if cyberparlement_member['idpersonne'] == id_user:
                user_cyberparlement_list.append(cyberparlement)
                try:
                    if Membrecp.objects.get(
                            cyberparlement=cyberparlement['idcyberparlement'],
                            personne=cyberparlement_member['idpersonne']).rolemembrecyberparlement == ROLE_CYBERCHANCELIER_KEY:
                        cyberparlement_children = get_cyberparlement_children(cyberparlements, cyberparlement['idcyberparlement'])
                        if cyberparlement_children is not None:
                            user_cyberparlement_list.extend(cyberparlement_children)
                except Membrecp.DoesNotExist:
                    pass
    return sorted([dict(t) for t in {tuple(d.items()) for d in user_cyberparlement_list if d}], key=lambda k: k['nom'])


class IndexView(ListView):
    '''
    La vue de la page d'accueil permettant d'insérer
    l'id de la personne sélectionnée dans la session
    '''
    template_name = 'cyberP/index.html'
    context_object_name = 'personnes'
    model = Personne

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))
        self.request.session['id_user'] = data['person_selected_id']
        return JsonResponse(data)


class CyberparlementListView(TemplateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = get_cyberparlement_list_printed(
            get_user_cyberparlement_list(int(self.request.session['id_user'])),
            self.request.session['id_user']
        )
        return context


class CyberparlementUpdateView(UpdateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_update.html'
    form_class = CyberparlementChangeForm
    model = Cyberparlement

    def get_id_person_selected(self):
        if self.request.method == 'POST':
            data = json.loads(self.request.body.decode('utf-8'))
            return data['person_selected_id']
        return None

    def get_current_cyberchancelier(self):
        try:
            member = Membrecp.objects.get(
                cyberparlement_id=self.kwargs['pk'],
                rolemembrecyberparlement=ROLE_CYBERCHANCELIER_KEY
            )
        except Membrecp.DoesNotExist:
            member = None
        return member

    def delete_current_cyberchancelier(self):
        current_cyberchancelier = self.get_current_cyberchancelier()
        current_cyberchancelier.rolemembrecyberparlement = ROLE_MEMBER_KEY
        current_cyberchancelier.save()

    def set_cyberchancelier(self):
        if self.get_id_person_selected():
            if self.get_current_cyberchancelier():
                self.delete_current_cyberchancelier()
            try:
                member_selected = Membrecp.objects.get(
                    personne_id=self.get_id_person_selected(),
                    cyberparlement_id=self.kwargs['pk']
                )
                member_selected.rolemembrecyberparlement = ROLE_CYBERCHANCELIER_KEY
                member_selected.save()
            except Membrecp.DoesNotExist:
                member_selected = Membrecp(
                    personne_id=self.get_id_person_selected(),
                    cyberparlement_id=self.kwargs['pk'],
                    rolemembrecyberparlement=ROLE_CYBERCHANCELIER_KEY
                )
                member_selected.save()

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("cyberP:cyberparlement-list")

    def get_context_data(self, **kwargs):
        self.set_cyberchancelier()
        context = super().get_context_data(**kwargs)
        context['members'] = get_cyberparlement_member_list(self.kwargs['pk'])
        return context


class CyberparlementCreateView(CreateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_add.html'
    form_class = CyberparlementCreationForm
    model = Cyberparlement

    def form_valid(self, form):
        cyberparlementparent = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        form.instance.cyberparlementparent = cyberparlementparent
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("cyberP:cyberparlement-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cyberparlement'] = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        return context


class CyberparlementMoveView(TemplateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_move.html'

    def get_cyberparlement_list_move_printed(self, cyberparlement_list):
        global content_move
        content_move = ''
        renderer = render_to_string('cyberP/cyberparlements/includes/cyberparlement_move_container_list.html')
        cyberchancelier_list = get_cyberchancelier_list()
        for cyberparlement in cyberparlement_list:
            for cyberchancelier in cyberchancelier_list:
                if cyberparlement['idcyberparlement'] == cyberchancelier['idcyberparlement']:
                    cyberparlement['cyberchancelier'] = cyberchancelier['person']
        for cyberparlement in cyberparlement_list:
            if cyberparlement['idcyberparlement'] == self.kwargs['pk']:
                cyberparlement_list.remove(cyberparlement)
        return print_cyberparlement_list_move_tree(parse_cyberparlement_tree(cyberparlement_list, None, self.kwargs['pk']), renderer)

    def set_new_parent(self, parent_id):
        cyberparlement = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        cyberparlement.cyberparlementparent_id = parent_id
        cyberparlement.save()

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))
        self.set_new_parent(data['cyberparlement_selected_id'])
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cyberparlement'] = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        context['content'] = self.get_cyberparlement_list_move_printed(get_user_cyberparlement_list(int(self.request.session['id_user'])))
        return context


class MemberListView(TemplateView):
    template_name = 'cyberP/members/member_list.html'

    def get_cyberparlement_member_list_with_rules(self):
        persons = get_cyberparlement_member_list(self.kwargs['pk'])
        members = list(Membrecp.objects.values())
        for member in members:
            for person in persons:
                if person['idpersonne'] == member['personne_id']:
                    person['role'] = member['rolemembrecyberparlement']
                    person['idmembrecyberparlement'] = member['idmembrecyberparlement']
        return persons

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = self.get_cyberparlement_member_list_with_rules()
        context['cyberchancelier'] = ROLE_CYBERCHANCELIER_KEY
        context['cyberparlement'] = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        return context


class MemberDeleteView(DeleteView):
    model = Membrecp
    template_name = 'cyberP/members/member_confirm_delete.html'

    def get_member_fullname(self):
        person = Membrecp.objects.get(idmembrecyberparlement=self.kwargs['pk']).personne
        return '{} {}'.format(person.prenom, person.nom)

    def get_success_url(self):
        return reverse_lazy("cyberP:cyberparlement-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person_fullname'] = self.get_member_fullname()
        return context
