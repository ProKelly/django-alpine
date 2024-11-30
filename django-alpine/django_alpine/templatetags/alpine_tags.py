# django_alpine/templatetags/alpine_tags.py
from django import template
from django.conf import settings
import os

register = template.Library()

@register.simple_tag
def alpine_js():
    """Return the path to the locally hosted Alpine.js file."""
    static_dir = os.path.join(settings.STATIC_URL, "js", "alpine.js")
    return static_dir
