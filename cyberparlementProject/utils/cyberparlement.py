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
                root.id if root is not None else None):
            if child.cyberparlementparent_id == (
                    root.id if root is not None else None):
                child.enfant = parse_cyberparlement_tree(
                    tree,
                    child,
                    id_cyberparlement_selected
                )
                res.append(child)
    return res or None


def print_cyberparlement_tree(tree, template, content_tree: list, request=None, member=None):
    """
    retourne la liste des cyberparlements
    de façon hiérarchique sous format html dans une string
    """
    if tree is not None and len(tree) > 0:
        if tree is None:
            return
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
                node.enfant,
                template,
                content_tree,
                request,
                member
            )
            content_tree.append('</div>')
        content_tree.append('</div>')
    return content_tree


def get_cyberparlement_id_by_slug(slug_cyberparlement):
    """
    retourne l'id d'un cyberparlement
    en fonction de son slug
    """
    try:
        return Cyberparlement.objects.get(slug=slug_cyberparlement).id
    except Cyberparlement.DoesNotExist:
        return None
