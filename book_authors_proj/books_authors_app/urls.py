from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.add_object_page),
    path('books', views.add_object_page),
    path('<str:table>/<int:id>', views.info_page),
    path('add_object', views.add_object),
    path('delete_object', views.delete_object),
    path('attach_object', views.attach_object),
]