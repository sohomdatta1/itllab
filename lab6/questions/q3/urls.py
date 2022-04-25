
from django.urls import path
from . import views

urlpatterns = [
        path('login', views.login, name='login'),
        path('home', views.home, name='home')
    ]