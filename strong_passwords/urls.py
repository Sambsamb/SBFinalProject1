"""
INF601 - Advanced Programming in Python
Final Project - App relating to MPS concentration
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
12/4/2022
"""

from django.urls import path
from strong_passwords import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check_email/', views.check_email, name='check_email'),
    path('about/', views.about, name='about'),
]


