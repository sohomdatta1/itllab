
from django.urls import path
from . import views
urlpatterns = [
    path('', views.input, name='index_q4'),
    path('output', views.output, name='output_q4')
    ]