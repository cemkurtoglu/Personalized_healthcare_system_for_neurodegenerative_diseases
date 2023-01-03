from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def get_prediction_name(value):

    if value == "0":
        return "MCI"
    elif value == "1":
        return "AD"
    return ""
