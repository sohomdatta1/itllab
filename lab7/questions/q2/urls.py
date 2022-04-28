
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register_work', views.register_work, name='register_work'),
    path('register_live', views.register_live, name='register_live'),
    path('get_for_company', views.get_for_company, name='gfc')
    ]