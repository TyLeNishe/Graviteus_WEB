import base64

from django import template

register = template.Library()


@register.filter
def base64_encode(value):
    if isinstance(value, str):
        value = value.encode('utf-8')
    return base64.b64encode(value).decode('utf-8')
