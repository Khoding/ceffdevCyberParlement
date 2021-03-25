from django.http import JsonResponse, request, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from .models import Cyberparlement, Membrecp, Personne, ROLE_MEMBER_KEY, ROLE_CYBERCHANCELIER_KEY, \
    STATUS_POSTED_KEY, STATUS_DRAFT_KEY, VISIBILITY_PUBLIC_KEY, VISIBILITY_PRIVATE_KEY, VISIBILITY_PUBLIC_VALUE, VISIBILITY_PRIVATE_VALUE
from .forms import CyberparlementChangeForm, CyberparlementCreationForm

import json

content = ''


def cleaned_data(l):
    """
    fonction retournant la liste mise en paramètre
    sans doublon et ordonné par nom
    """
    return sorted([dict(t) for t in {tuple(d.items()) for d in l if d}], key=lambda k: k['nom'])


def get_cyberchancelier_list():
    """
    fonction retournant tous les cyberchanceliers
    """
    members = list(Membrecp.objects.values())
    persons = list(Personne.objects.values())
    return [{'person': person,
             'idcyberparlement': member['cyberparlement_id']}
            for person in persons for member in members
            if member['personne_id'] == person['idpersonne']
            and member['rolemembrecyberparlement'] == ROLE_CYBERCHANCELIER_KEY]


def get_cyberparlement_parent(cyberparlements, id_cyberparlementparent):
    """
    fonction récursive retournant tous les
    cyberparlements parents d'un cyberparlement
    """
    res = []
    for cyberparlement in cyberparlements:
        if cyberparlement['idcyberparlement'] == id_cyberparlementparent:
            res.append(cyberparlement)
            next_result = get_cyberparlement_parent(
                cyberparlements,
                cyberparlement['cyberparlementparent_id']
            )
            if next_result is not None:
                res.extend(next_result)
    return res if res else None


def get_cyberparlement_children(cyberparlements, id_cyberparlement):
    """
    fonction récursive retournant tous les
    cyberparlements enfants d'un cyberparlement
    """
    res = []
    for cyberparlement in cyberparlements:
        if cyberparlement['cyberparlementparent_id'] == id_cyberparlement:
            res.append(cyberparlement)
            next_result = get_cyberparlement_children(
                cyberparlements,
                cyberparlement['idcyberparlement']
            )
            if next_result is not None:
                res.extend(next_result)
    return res if res else None


def get_cyberparlement_cyberchancelier(id_cyberparlement):
    """
    fonction retourant le cybcerchancelier
    d'un cyberparleent
    """
    if get_cyberchancelier_list() is not None:
        for cyberchancelier in get_cyberchancelier_list():
            if cyberchancelier['idcyberparlement'] == id_cyberparlement:
                return cyberchancelier['person']
    return None


def get_cyberparlement_all_cyberchancelier_list(cyberparlement_selected):
    """
    fonction retournant tous les cyberchancelier
    qui ont accès à un cyberparlement
    """
    res = [get_cyberparlement_cyberchancelier(cyberparlement_selected['idcyberparlement'])]
    cyberparlements = get_cyberparlement_parent(
        list(Cyberparlement.objects.values()),
        cyberparlement_selected['cyberparlementparent_id']
    )
    if cyberparlements is not None:
        for cyberparlement in cyberparlements:
            res.append(get_cyberparlement_cyberchancelier(cyberparlement['idcyberparlement']))
    return cleaned_data(res)


def parse_cyberparlement_tree(tree, root, id_cyberparlement_selected):
    """
    fonction récursive retournant une liste
    des cyberparlements sous forme d'arborescence
    """
    res = []
    for child in tree:
        if id_cyberparlement_selected != (
                root['idcyberparlement'] if root is not None else None):
            if child['cyberparlementparent_id'] == (
                    root['idcyberparlement'] if root is not None else None):
                child['enfant'] = parse_cyberparlement_tree(
                    tree,
                    child,
                    id_cyberparlement_selected
                )
                child['allcyberchancelier'] = \
                    get_cyberparlement_all_cyberchancelier_list(child)
                res.append(child)
    return res if res else None


def print_cyberparlement_tree(tree, template, id_user=None):
    """
    fonction récursive retournant la liste
    des cyberparlements de façon hiérarchique
    """
    global content
    if tree is not None and len(tree) > 0:
        content += '<div class=cp-list-container>'
        for node in tree:
            content += render_to_string(
                template,
                {
                    'cyberparlement': node,
                    'iduser': id_user,
                    'privatevisibilitykey': VISIBILITY_PRIVATE_KEY,
                    'publicvisibilityvalue': VISIBILITY_PUBLIC_VALUE,
                    'privatevisibilityvalue': VISIBILITY_PRIVATE_VALUE,
                    'draftstatuskey': STATUS_DRAFT_KEY
                }
            )
            print_cyberparlement_tree(
                node['enfant'],
                template,
                id_user
            )
            content += '</div>'
        content += '</div>'
    return content


def get_cyberparlement_member_list(id_cyberparlement):
    """
    fonction retournant une liste de
    tous les membres d'un cyberparlement
    """
    members = list(Membrecp.objects.filter(cyberparlement=id_cyberparlement).values())
    persons = list(Personne.objects.order_by('nom').values())
    cyberparlements = get_cyberparlement_children(list(Cyberparlement.objects.values()), id_cyberparlement)
    if cyberparlements is not None:
        for cyberparlement in cyberparlements:
            cyberparlement_members = list(Membrecp.objects.filter(cyberparlement=cyberparlement['idcyberparlement']).values())
            if cyberparlement_members is not None:
                members.extend(cyberparlement_members)
    persons = [person for person in persons for member in members if member['personne_id'] == person['idpersonne']]
    return cleaned_data(persons)


def get_user_cyberparlement_list(id_user):
    """
    fonction retournant une liste de tous
    les cyberparlements que l'utilisateur a accès
    """
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
    return cleaned_data(user_cyberparlement_list)


class IndexView(ListView):
    """
    vue de la page d'accueil permettant d'insérer
    l'id de la personne sélectionnée dans la session
    """
    template_name = 'cyberP/index.html'
    context_object_name = 'personnes'
    model = Personne

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))
        self.request.session['id_user'] = data['person_selected_id']
        return HttpResponseRedirect(reverse('cyberP:cyberparlement-list'))


class CyberparlementListView(TemplateView):
    """
    vue de la page permettant de consulter
    la liste des cyberparlements
    """
    template_name = 'cyberP/cyberparlements/cyberparlement_list.html'

    def get_cyberparlement_list_printed(self, cyberparlement_list):
        """
        méthode retournant la liste des cyberparlements
        de façon hiérarchique utilisée pour la consultation
        de la liste des cyberparlements
        """
        global content
        content = ''
        for cyberparlement in cyberparlement_list:
            for cyberchancelier in get_cyberchancelier_list():
                if cyberparlement['idcyberparlement'] == cyberchancelier['idcyberparlement']:
                    cyberparlement['cyberchancelier'] = cyberchancelier['person']
        return print_cyberparlement_tree(
            parse_cyberparlement_tree(cyberparlement_list, None, 0),
            'cyberP/cyberparlements/includes/cyberparlement_container_list.html',
            self.request.session['id_user']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'id_user' in self.request.session:
            context['content'] = self.get_cyberparlement_list_printed(
                get_user_cyberparlement_list(
                    int(self.request.session['id_user'])
                )
            )
        else:
            context['content'] = "Sélectionnez un utilisateur"
        return context


class CyberparlementUpdateView(UpdateView):
    """
    vue permettant de modifier les données d'un cyberparlement
    """
    template_name = 'cyberP/cyberparlements/cyberparlement_update.html'
    form_class = CyberparlementChangeForm
    model = Cyberparlement
    success_url = reverse_lazy("cyberP:cyberparlement-list")

    def get_id_person_selected(self):
        """
        méthode retournant l'id de la personne sélectionné
        afin de devenir cyberchancelier
        """
        if self.request.method == 'POST':
            data = json.loads(self.request.body.decode('utf-8'))
            return data['person_selected_id']
        return None

    def get_current_cyberchancelier(self):
        """
        méthode retournant le cyberchancelier actuel du cyberparlement
        """
        try:
            member = Membrecp.objects.get(
                cyberparlement_id=self.kwargs['pk'],
                rolemembrecyberparlement=ROLE_CYBERCHANCELIER_KEY
            )
        except Membrecp.DoesNotExist:
            member = None
        return member

    def delete_current_cyberchancelier(self):
        """
        méthode modifiant dans la base de données
        le rôle du cyberchancelier actuel du cyberparlement
        """
        current_cyberchancelier = self.get_current_cyberchancelier()
        current_cyberchancelier.rolemembrecyberparlement = ROLE_MEMBER_KEY
        current_cyberchancelier.save()

    def set_cyberchancelier(self):
        """
        méthode modifiant dans la base de données
        le nouveau cyberchancelier du cyberparlement
        """
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

    def get_context_data(self, **kwargs):
        self.set_cyberchancelier()
        context = super().get_context_data(**kwargs)
        context['members'] = get_cyberparlement_member_list(self.kwargs['pk'])
        return context


class CyberparlementCreateView(CreateView):
    """
    vue permettant de créer un nouveau cyberparlement
    à l'intérieur d'un cyberparlement
    """
    template_name = 'cyberP/cyberparlements/cyberparlement_add.html'
    form_class = CyberparlementCreationForm
    model = Cyberparlement
    success_url = reverse_lazy("cyberP:cyberparlement-list")

    def form_valid(self, form):
        """
        méthode appelé lors de la validation de la création d'un cyberparlement
        qui va ajouter le cyberparlement parent dans le nouveau cyberparlement
        """
        cyberparlementparent = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        form.instance.cyberparlementparent = cyberparlementparent
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cyberparlement'] = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        return context


class CyberparlementMoveView(TemplateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_move.html'

    def get_cyberparlement_list_move_printed(self, cyberparlement_list):
        """
        méthode retournant la liste des cyberparlements
        de façon hiérarchique utilisée pour le déplacement
        d'un cyberparlement dans la structure
        """
        global content
        content = ''
        for cyberparlement in cyberparlement_list:
            for cyberchancelier in get_cyberchancelier_list():
                if cyberparlement['idcyberparlement'] == cyberchancelier['idcyberparlement']:
                    cyberparlement['cyberchancelier'] = cyberchancelier['person']
        for cyberparlement in cyberparlement_list:
            if cyberparlement['idcyberparlement'] == self.kwargs['pk']:
                cyberparlement_list.remove(cyberparlement)
        return print_cyberparlement_tree(
            parse_cyberparlement_tree(cyberparlement_list, None, self.kwargs['pk']),
            'cyberP/cyberparlements/includes/cyberparlement_move_container_list.html'
        )

    def set_new_parent(self, parent_id):
        """
        méthode permettant de modifier
        le cyberparlement parent d'un cyberparlement
        """
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
    """
    vue permettant de consulter la liste
    des membres d'un cyberparlement
    """
    template_name = 'cyberP/members/member_list.html'

    def get_cyberparlement_member_list_with_rules(self):
        """
        méthode retournant les membres du cyberparlement
        avec leurs rôles dans ce dernier
        """
        persons = get_cyberparlement_member_list(self.kwargs['pk'])
        members = list(Membrecp.objects.values())
        for member in members:
            for person in persons:
                if person['idpersonne'] == member['personne_id']:
                    person['role'] = member['rolemembrecyberparlement']
                    person['idmembrecyberparlement'] = member['idmembrecyberparlement']
        return cleaned_data(persons)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = self.get_cyberparlement_member_list_with_rules()
        context['cyberchancelier'] = ROLE_CYBERCHANCELIER_KEY
        context['cyberparlement'] = Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk'])
        return context


class MemberDeleteView(DeleteView):
    """
    vue permettant la suppression
    d'un membre d'un cyberparlement
    """
    model = Membrecp
    template_name = 'cyberP/members/member_confirm_delete.html'
    success_url = reverse_lazy("cyberP:cyberparlement-list")

    def get_member_fullname(self):
        """
        méthode retournant le nom complet
        du membre à supprimer
        """
        person = Membrecp.objects.get(idmembrecyberparlement=self.kwargs['pk']).personne
        return '{} {}'.format(person.prenom, person.nom)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person_fullname'] = self.get_member_fullname()
        return context
