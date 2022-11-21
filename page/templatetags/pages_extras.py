from ..models import Page
from django import template

#registrar template
register = template.Library()

#decorador
@register.simple_tag

#consultar todas las paginas secundarias
def get_pages_list():
    pages=Page.objects.all()
    return pages