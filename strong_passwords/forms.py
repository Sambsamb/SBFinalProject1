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
    check_email = forms.EmailField(required=True,
                                   label='Email address',
                                   # initial='Enter email',
                                   help_text='<small id="emailHelp" class="form-text text-muted">'
                                             'Email is not stored. See '
                                             '<a href ="/policy" target=_blank>Privacy Policy</a>.</small>',
                                   max_length=100,
                                   )


class CheckPass(forms.Form):
    check_pass = forms.CharField(required=True,
                                   label='Password',
                                   # initial='Enter email',
                                   help_text='<small id="emailHelp" class="form-text text-muted">'
                                             'Password is not stored. See '
                                             '<a href ="/policy" target=_blank>Privacy Policy</a>.</small>',
                                   max_length=100,
                                   )