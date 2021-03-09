from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from .models import Cyberparlement, Membrecp, Personne
from .forms import CyberparlementChangeForm

url = 'http://127.0.0.1:8000'
content = ''


class IndexView(ListView):
    template_name = 'cyberP/index.html'
    context_object_name = 'personnes'
    model = Personne


# class FirstCyberparlementListView(ListView):
#     template_name = 'cyberP/cyberparlements/cyberparlement_list.html'
#     context_object_name = 'cyberparlements'
#     model = Cyberparlement
#
#     def get_queryset(self):
#         return self.model.objects.filter(cyberparlementparent=None)


# class CyberparlementDetailView(DetailView):
#     template_name = 'cyberP/cyberparlements/cyberparlement_detail.html'
#     model = Cyberparlement
#
#     def get_context_data(self, **kwargs):
#         cyberparlements = Cyberparlement.objects.filter(cyberparlementparent=self.kwargs['pk'])
#         context = super().get_context_data(**kwargs)
#         context['cyberparlements'] = cyberparlements
#         return context


def parse_tree(tree, root=None):
    res = []
    for child in tree:
        if child['cyberparlementparent_id'] == (root['idcyberparlement'] if root is not None else None):
            res.append(
                {
                    'idcyberparlement': child['idcyberparlement'],
                    'nom': child['nom'],
                    'description': child['description'],
                    'enfant': parse_tree(tree, child)
                }
            )
    return res if res else None


def print_tree(tree):
    global content
    if tree is not None and len(tree) > 0:
        content += '<div style=padding:10px;>'
        for node in tree:
            content += '<div style=padding:10px;border-style:solid;margin-bottom:10px>{}<br>{}' \
                       '    <a href={}/cyberparlements/{}/update>' \
                       '        <button> Modifier </button>' \
                       '    </a>'.format(node['nom'], node['description'], url, node['idcyberparlement'])
            print_tree(node['enfant'])
            content += '</div>'
        content += '</div>'
    return content


result = print_tree(parse_tree(list(Cyberparlement.objects.values())))


class CyberparlementListView(TemplateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = result
        return context


class CyberparlementUpdateView(UpdateView):
    template_name = 'cyberP/cyberparlements/cyberparlement_update.html'
    form_class = CyberparlementChangeForm
    model = Cyberparlement

    def get_cyberparlement_member(self):
        members = list(Membrecp.objects.filter(cyberparlement=self.kwargs['pk']).values())
        persons = list(Personne.objects.values())
        return [person for person in persons for member in members if member['personne_id'] == person['idpersonne']]

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("cyberP:cyberparlement-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = self.get_cyberparlement_member()
        return context


class MemberListView(ListView):
    template_name = 'cyberP/members/member_list.html'
    model = Personne
