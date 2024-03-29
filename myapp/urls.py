from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('', views.get_home, name='home'),
    path('about/', views.get_about, name='about'),
    path('case-studies/', views.get_logos, name='case-studies'),
    path('portfolio/', views.get_portfolio, name='portfolio'),
    path('contact/', views.get_contact, name='contact')
]
