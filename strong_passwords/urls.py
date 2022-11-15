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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('check_email/', views.check_email, name='check_email'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact, name='contact'),
    path('dataclasses/', views.data_classes, name='data_classes'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "strong_passwords.views.page_not_found_view"
