from django import template

register = template.Library()

from datetime import datetime

@register.filter(name='day_diff')
def day_diff(a_date):
    today = int(datetime.now().strftime("%d"))
    return today - a_date.day

# for debugging
@register.simple_tag(takes_context=True)
def set_breakpoint(context):
    breakpoint()
