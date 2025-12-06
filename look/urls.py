from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.look_home, name='look_home'),
    path('edit', views.edit, name='edit'),
]
