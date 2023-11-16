# custom_filters.py
from django import template
import os

register = template.Library()

@register.filter()
def filename(value):
    return os.path.basename(value)

def replace_backslashes(value):
    return value.replace('\\', '/')