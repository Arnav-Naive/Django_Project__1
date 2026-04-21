from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def highlight(text, query):
    if not query:
        return text
    escaped_text = escape(text)
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    highlighted = pattern.sub(
        lambda m: f'<mark style="background-color: violet;">{m.group()}</mark>',
        escaped_text
    )
    return mark_safe(highlighted)