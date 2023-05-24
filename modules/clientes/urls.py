from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'clientes'

urlpatterns = [
    path('add-client/',
         views.AddClient.as_view(), name='add-client'),
    path('add-filial/',
         views.AddFilial.as_view(), name='add-filial'),
    path('list-filial/',
         views.ListFilial.as_view(), name='list-filial'),
    path('update-filial/', views.UpdateFilial.as_view(), name='update-filial')
]
