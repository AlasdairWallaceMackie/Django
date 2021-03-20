from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

def index(request):
    print( "Counter: " + str(request.session['counter']) )

    return render(request, 'index.html')


def generate(request):
    print("Generate clicked")
    request.session['counter'] += 1
    word = get_random_string(14)
    print("Word: " + word)
    request.session['generated_word'] = get_random_string(14)
    return redirect('/')

def reset(request):
    request.session['counter'] = 1
    request.session['generated_word'] = ""
    return redirect('/')