from django.contrib import admin
from django.urls import path

# we need to import views from our contact app
from contact import views

urlpatterns = [
  path('', views.index, name='index'),
]
