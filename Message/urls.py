# example/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login-admin/', views.loginAdmin, name='loginAdmin'),
    path('message-page/', views.messageAdmin, name='messageAdmin')
]