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
from django.contrib import messages


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
            # redirect to a new URL:
            return HttpResponseRedirect('/check_email/')
        messages.success(request, 'Unsuccessful registration. Invalid information.')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckEmail()

    return render(request, 'check_email.html', {'form': form})
