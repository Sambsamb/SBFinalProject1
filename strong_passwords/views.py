"""
INF601 - Advanced Programming in Python
Final Project - App relating to MPS concentration
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
12/4/2022
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CheckEmail
from .functions import *
import Config
from django.contrib import messages
import datetime
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def home(request):
    return render(request, 'home.html', {'site_name': Config.site_name})


def check_email(request):
    # if this is a POST request process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CheckEmail(request.POST)
        # check whether it's valid:
        if form.is_valid():
            check_result = check_email_function(form.cleaned_data['check_email'])
            keys = set()
            for item in check_result:
                keys.update(set(item))
            key_order = sorted(keys)
            context = {
                'email': form.cleaned_data['check_email'],
                'check_result': check_result,
                'key_order': key_order,
                'site_name': Config.site_name,
            }
        return render(request, 'check_email.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckEmail()
        context = {
            'form': form,
            'site_name': Config.site_name,
        }
        return render(request, 'check_email.html', context)
