from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path("login/", views.login_request, name="login"),
]
