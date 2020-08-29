from django import template

register = template.Library()


@register.filter
def header_top_style(path):
  if 'ask' in path:
    return 'ask'
  return ''
