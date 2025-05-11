from django import template

register = template.Library()

@register.filter
def is_default_image(value):
    """Return True if the image URL ends with 'list.jpeg'"""
    if not isinstance(value, str):
        return False
    return value.endswith('list.jpeg')
