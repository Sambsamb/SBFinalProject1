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
from django.contrib import messages
import datetime


def home(request):
    return render(request, 'home.html', {})


def check_email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CheckEmail(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # https://docs.djangoproject.com/en/4.1/ref/contrib/messages/
            messages.info(request, '"%s" is the received form input' % form.cleaned_data['check_email'])
            check_result = check_email_function(form.cleaned_data['check_email'])
            messages.info(request, 'Check result:')
            if type(check_result) == list:
                for result in check_result:
                    for key in result.keys():
                        # Convert Date fields from UTC to current time zone
                        try:
                            myout1 = str(key).ljust(12) + str(datetime.datetime.strptime(str(result[key]), '%Y-%m-%dT%H:%M:%SZ'))
                        except:
                            myout1 = str(key).ljust(12) + str(result[key])
                        messages.info(request, myout1)
            else:
                myout1 = str(check_result)
            messages.info(request, myout1)
            # redirect to a new URL:
            return HttpResponseRedirect('/check_email/')
        messages.success(request, 'Unsuccessful registration. Invalid information.')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckEmail()

    return render(request, 'check_email.html', {'form': form})
