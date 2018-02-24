# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail, name='detail')
]
