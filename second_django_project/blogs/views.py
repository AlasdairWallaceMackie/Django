from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return HttpResponse('<h1>Blogs app is up</h1><p>Placeholder to later display a list of all blogs</p>')

def new(request):
    return HttpResponse('Placeholder to display a new form to create a <span style="color: red">NEW</span> blog')

def create(request):
    return redirect('/blogs')

def show(request, number):
    return HttpResponse(f'Placeholder to display blog number: {number}')

def edit(request, number):
    return HttpResponse(f'Placeholder to <span style="color: red">EDIT</span> blog: {number}')

def destroy(request, number):
    return redirect('/blogs')
