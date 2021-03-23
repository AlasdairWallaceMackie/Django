from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>Surveys</h1>Placeholder to display all the surveys created')

def new(request):
    return HttpResponse('<h1>Surveys</h1>Placeholder for users to adda a <span style="color: red">NEW</span> survey')
