
from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('register_cat', views.register_cat, name='register_cat'),
        path('register_page', views.register_page, name='register_page')
    ]