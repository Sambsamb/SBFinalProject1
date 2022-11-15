"""
INF601 - Advanced Programming in Python
Final Project - App relating to MPS concentration
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
12/4/2022
"""

from .forms import *
from .functions import *
import Config
from django.shortcuts import render
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def home(request):
    return render(request, 'home.html', {'site_name': Config.site_name})


def about(request):
    return render(request, 'about.html', {'site_name': Config.site_name})


def policy(request):
    return render(request, 'policy.html', {'site_name': Config.site_name})


def contact(request):
    return render(request, 'contact.html', {'site_name': Config.site_name})


def data_classes(request):
    context = {
        'data_classes_list': get_hibp_dataclasses_function(),
        'site_name': Config.site_name,
    }
    return render(request, 'dataclasses.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def server_error_view(request):
    return render(request, '500.html')


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
            code = text = detail = None
            alert = 'danger'
            if type(check_result) == dict:
                key_order = None
                code = check_result['code']
                text = check_result['text']
                if check_result['code'] == 400:
                    detail = 'Bad request: The email provided does not comply with acceptable format.'
                    alert = 'warning'
                elif check_result['code'] == 401:
                    detail = 'Unauthorized — the API key provided was not valid.'
                    alert = 'warning'
                elif check_result['code'] == 403:
                    detail = 'Forbidden: No user agent has been specified in the request.'
                    alert = 'danger'
                elif check_result['code'] == 404:
                    detail = 'Not found in breach data.'
                    alert = 'success'
                elif check_result['code'] == 429:  # Rate limit exceeded
                    detail = check_result['json']['message']
                    alert = 'info'
                else:
                    detail = 'Unexpected status code.'
                    alert = 'warning'
            context = {
                'email': form.cleaned_data['check_email'],
                'check_result': check_result,
                'key_order': key_order,
                'code': code,
                'text': text,
                'detail': detail,
                'alert': alert,
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


def check_pass(request):
    # if this is a POST request process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CheckPass(request.POST)
        # check whether it's valid:
        if form.is_valid():
            check_result = check_pass_function(form.cleaned_data['check_pass'])
            try:
                prevalence = '{:,}'.format(int(check_result.split(':')[1]))
            except:
                prevalence = 0
            context = {
                'check_result': check_result,
                'prevalence': prevalence,
                'pass': form.cleaned_data['check_pass'],
                'site_name': Config.site_name,
            }
        return render(request, 'check_pass.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckPass()
        context = {
            'form': form,
            'site_name': Config.site_name,
        }
        return render(request, 'check_pass.html', context)
