# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 19:31
# @Author  : Endless-cloud
# @Site    : 
# @File    : my_tags.py
# @Software: PyCharm
from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变


@register.simple_tag
def simple_tag_multi(v1, v2):

    return v1 * v2
