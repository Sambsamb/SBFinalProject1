"""
INF601 - Advanced Programming in Python
Final Project - App relating to MPS concentration
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
12/4/2022
"""

from django import forms


class CheckEmail(forms.Form):
    check_email = forms.CharField(label='Email', max_length=100)
