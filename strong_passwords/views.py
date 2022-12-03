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
import time


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
            code1 = text1 = detail1 = None
            alert1 = 'danger'
            if type(check_result) == dict:
                key_order = None
                code1 = check_result['code']
                text1 = check_result['text']
                if check_result['code'] == 400:
                    detail1 = 'Bad request: The email provided does not comply with acceptable format.'
                    alert1 = 'warning'
                elif check_result['code'] == 401:
                    detail1 = 'Unauthorized — the API key provided was not valid.'
                    alert1 = 'warning'
                elif check_result['code'] == 403:
                    detail1 = 'Forbidden: No user agent has been specified in the request.'
                    alert1 = 'danger'
                elif check_result['code'] == 404:
                    detail1 = 'Not found in breach data.'
                    alert1 = 'success'
                elif check_result['code'] == 429:  # Rate limit exceeded
                    detail1 = check_result['json']['message']
                    alert1 = 'info'
                else:
                    detail1 = 'Unexpected status code.'
                    alert1 = 'warning'

            time.sleep(6)  # Need to wait 6 sec otherwise I get 429 (lowest API subscription)
            check_breaches = breachedaccount_function(form.cleaned_data['check_email'])
            code2 = text2 = detail2 = None
            alert2 = 'danger'
            breach_keys = [
                'Title',
                'Domain',
                'BreachDate',
                'PwnCount',
                'Description',
            ]
            if type(check_breaches) == dict:
                breach_keys = None
                code2 = check_breaches['code']
                text2 = check_breaches['text']
                if check_breaches['code'] == 400:
                    detail2 = 'Bad request: The email provided does not comply with acceptable format.'
                    alert2 = 'warning'
                elif check_breaches['code'] == 401:
                    detail2 = 'Unauthorized — the API key provided was not valid.'
                    alert2 = 'warning'
                elif check_breaches['code'] == 403:
                    detail2 = 'Forbidden: No user agent has been specified in the request.'
                    alert2 = 'danger'
                elif check_breaches['code'] == 404:
                    detail2 = 'Not found in breach data.'
                    alert2 = 'success'
                elif check_breaches['code'] == 429:  # Rate limit exceeded
                    detail2 = check_result['json']['message']
                    alert2 = 'info'
                else:
                    detail2 = 'Unexpected status code.'
                    alert2 = 'warning'


            context = {
                'email': form.cleaned_data['check_email'],
                'site_name': Config.site_name,

                'key_order': key_order,
                'check_result': check_result,
                'code1': code1,
                'text1': text1,
                'detail1': detail1,
                'alert1': alert1,

                'breach_keys': breach_keys,
                'check_breaches': check_breaches,
                'breach_count': len(check_breaches),
                'code2': code2,
                'text2': text2,
                'detail2': detail2,
                'alert2': alert2,
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


def breaches_view(request):
    breach_list = breaches_function()
    key_order = [
        'BreachDate',
        'Domain',
        'PwnCount',
        'IsFabricated',
        'IsMalWare',
        'IsSpamList',
        'IsVerified',
        'Description',
    ]
    context = {
        'breach_list': breach_list[:-1],  # All the list elements except the last one (summaries)
        'All': breach_list[-1]['All'],
        'IsFabricatedCount': breach_list[-1]['IsFabricatedCount'],
        'IsMalwareCount': breach_list[-1]['IsMalwareCount'],
        'IsRetiredCount': breach_list[-1]['IsRetiredCount'],
        'IsSensitiveCount': breach_list[-1]['IsSensitiveCount'],
        'IsSpamListCount': breach_list[-1]['IsSpamListCount'],
        'IsVerifiedCount': breach_list[-1]['IsVerifiedCount'],
        'key_order': key_order,
        'site_name': Config.site_name,
    }
    return render(request, 'breaches.html', context)
