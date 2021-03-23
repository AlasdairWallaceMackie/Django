from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('users/', views.users, name="users"),
    path('users/new/', views.new, name="new"),
]