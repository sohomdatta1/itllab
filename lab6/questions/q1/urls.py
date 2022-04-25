
from django.urls import path
from . import views 

urlpatterns = [
        path('input', views.input, name='input'),
        path('output', views.output, name='output'),
]