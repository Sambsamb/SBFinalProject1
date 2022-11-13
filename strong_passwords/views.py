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


def home(request):
    return render(request, 'home.html', {})


def check_email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CheckEmail(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/check_email/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckEmail()

    return render(request, 'check_email.html', {'form': form})
