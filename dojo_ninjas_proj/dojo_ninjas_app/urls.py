from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.add_dojo),
    path('add_ninja', views.add_ninja),
    path('delete', views.delete),
    path('get_dojos', views.get_dojos),
]
