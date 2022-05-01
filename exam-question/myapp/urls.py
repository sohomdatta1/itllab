
from django.urls import path
from . import views
urlpatterns = [
    path('1', views.index),
    path('1/results', views.results)
 ]