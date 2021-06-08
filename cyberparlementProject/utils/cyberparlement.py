from django.template.loader import render_to_string

from cyberparlementProject.models import Cyberparlement


def parse_cyberparlement_tree(tree, root, id_cyberparlement_selected):
    """
    retourne une liste des cyberparlements
    sous forme d'arborescence
    """
    res = []
    for child in tree:
        if id_cyberparlement_selected != (
                root.id if root else None):
            if child.cyberparlementparent_id == (
                    root.id if root else None):
                child.children = parse_cyberparlement_tree(
                    tree,
                    child,
                    id_cyberparlement_selected
                )
                res.append(child)
    return res or None


def print_cyberparlement_tree(tree, template, content_tree: list, request=None, member=None):
    """
    retourne la liste des cyberparlements
    de façon hiérarchique sous format html dans une list string
    """
    if tree and len(tree) > 0:
        content_tree.append('<div class=cp-list-container style=padding:10px>')
        for node in tree:
            content_tree.append(render_to_string(
                template_name=template,
                context={
                    'cyberparlement': node,
                    'member': member,
                },
                request=request
            ))
            print_cyberparlement_tree(
                node.children,
                template,
                content_tree,
                request,
                member
            )
            content_tree.append('</div>')
        content_tree.append('</div>')
    return content_tree
