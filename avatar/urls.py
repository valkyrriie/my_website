from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.avatar_home, name='avatar_home'),

]
