from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')

def register(request):
    return HttpResponse('<h1>Users</h1>Placeholder for users to create a <b>new user record</b>')

def login(request):
    return HttpResponse('<h1>Users</h1>Placeholder for users to <b>login</b>')

def users(request):
    return HttpResponse('<h1>Users</h1>Placeholder to display the list of all users')

def new(request):
    return redirect('/register')
