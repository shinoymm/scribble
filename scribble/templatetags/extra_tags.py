__author__ = 'shinoymm'

from django import template

register = template.Library()


def get_filename(value):
    return value.split('/')[-1]


def replace(value, arg):
    args = arg.split('|')
    return value.replace(args[0], args[1])


register.filter('get_filename', get_filename)
register.filter('replace', replace)