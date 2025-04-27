# custom_filters.py (в директории templatetags)

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Умножает value на arg"""
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0  # Возвращаем 0 в случае ошибки
