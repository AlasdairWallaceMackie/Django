from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *

def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        age = request.POST['age'],
    )
    return redirect('/')
