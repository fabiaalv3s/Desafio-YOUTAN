from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('add-client', views.CreateClient.as_view(), name='add-client'),
    path('update-client/<int:pk>/', views.UpdateClient.as_view(), name='update-client'),
    path('delete/<int:pk>/', views.DeleteClient.as_view(), name='delete-client')
]
