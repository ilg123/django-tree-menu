from django import template
from menu.models import Menu
from django.urls import resolve

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        request = context['request']
        current_url = resolve(request.path_info).url_name
        return {'menu': menu, 'current_url': current_url}
    except Menu.DoesNotExist:
        return {'menu': None, 'current_url': None}
