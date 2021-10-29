from django import template
from django.template import library
from Accounts.models import User_Profile

register = template.Library()

@register.inclusion_tag('accounts/user_img.hmtl')
def user_details():
    pass
   