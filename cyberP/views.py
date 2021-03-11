from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView
from .models import Cyberparlement, Membrecp, Personne, ROLE_MEMBER_KEY, ROLE_CYBERCHANCELIER_KEY
from .forms import CyberparlementChangeForm

import json

url = 'http://127.0.0.1:8000'
content = ''


class IndexView(ListView):
    template_name = 'cyberP/index.html'
    context_object_name = 'personnes'
    model = Personne


def parse_tree(tree, root=None):
    res = []
    for child in tree:
        if child['cyberparlementparent_id'] == (root['idcyberparlement'] if root is not None else None):
            res.append(
                {
                    'idcyberparlement': child['idcyberparlement'],
                    'nom': child['nom'],
                    'description': child['description'],
                    'cyberchancelier': child['cyberchancelier']['prenom'] + ' ' + child['cyberchancelier']['nom'] if 'cyberchancelier' in child else 'Aucun cyberchancelier sélectionné',
                    'enfant': parse_tree(tree, child)
                }
            )
    return res if res else None


def print_tree(tree):
    global content
    if tree is not None and len(tree) > 0:
        content += '<div style=padding:10px;border-style:solid;border-color:green;>'
        for node in tree:
            content += '<div style=padding:10px;border-style:solid;margin-bottom:10px><b>{}</b><br>Cyberchancelier: {}<br>{}' \
                       '    <a href={}/cyberparlements/{}/update>' \
                       '        <button> Modifier </button>' \
                       '    </a>'.format(node['nom'], node['cyberchancelier'], node['description'] if node['description'] else '', url, node['idcyberparlement'])
            print_tree(node['enfant'])
            content += '</div>'
        content += '</div>'
    return content


def get_cyberchancelier_list():
    members = list(Membrecp.objects.values())
    persons = list(Personne.objects.values())
    return [{'person': person,
             'idcyberparlement': member['cyberparlement_id']}
            for person in persons for member in members
            if member['personne_id'] == person['idpersonne'] and member['rolemembrecyberparlement'] == ROLE_CYBERCHANCELIER_KEY]


def get_cyberparlement_list():
    global content
    content = ''
    cyberparlement_list = list(Cyberparlement.objects.values())
    cyberchancelier_list = get_cyberchancelier_list()
    for cyberparlement in cyberparlement_list:
        for cyberchancelier in cyberchancelier_list:
            if cyberparlement['idcyberparlement'] == cyberchancelier['idcyberparlement']:
                cyberparlement['cyberchancelier'] = cyberchancelier['person']

    return print_tree(parse_tree(cyberparlement_list))


class CyberparlementListView(TemplateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = get_cyberparlement_list()
        return context


class CyberparlementUpdateView(UpdateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_update.html'
    form_class = CyberparlementChangeForm
    model = Cyberparlement

    def get_cyberparlement_member_list(self):
        members = list(Membrecp.objects.filter(cyberparlement=self.kwargs['pk']).values())
        persons = list(Personne.objects.values())
        return [person for person in persons for member in members if member['personne_id'] == person['idpersonne']]

    def get_id_person_selected(self):
        res = None
        if self.request.method == 'POST':
            data = json.loads(self.request.body.decode('utf-8'))
            res = data['person_selected_id']
        return res

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
            member_selected = Membrecp.objects.get(
                personne_id=self.get_id_person_selected(),
                cyberparlement_id=Cyberparlement.objects.get(idcyberparlement=self.kwargs['pk']).idcyberparlement
            )
            member_selected.rolemembrecyberparlement = ROLE_CYBERCHANCELIER_KEY
            member_selected.save()

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("cyberP:cyberparlement-list")

    def get_context_data(self, **kwargs):
        self.set_cyberchancelier()
        context = super().get_context_data(**kwargs)
        context['members'] = self.get_cyberparlement_member_list()
        return context


class MemberListView(ListView):
    template_name = 'cyberP/members/member_list.html'
    model = Personne
