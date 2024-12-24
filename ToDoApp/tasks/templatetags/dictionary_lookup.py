# tasks/templatetags/dictionary_lookup.py
from django import template

register = template.Library()

@register.filter
def dictlookup(dictionary, key):
    return dictionary[key]
