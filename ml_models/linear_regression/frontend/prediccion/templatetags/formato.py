from django import template

register = template.Library()

@register.filter
def cop(valor):
    try:
        return "$ {:,.0f}".format(float(valor)).replace(",", ".")
    except (TypeError, ValueError):
        return valor