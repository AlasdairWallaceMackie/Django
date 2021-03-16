from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):

    if request.method=="POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']

        request.session['gender'] = request.POST['gender']

        drink_list = request.POST.getlist('drink')
        request.session['drink'] = "" ## <-- Have to initialize dict key here otherwise it throws a KeyError Exception
        for i in range ( len(drink_list) ):
            request.session['drink'] += drink_list[i]
            if i != len(drink_list)-1:
                request.session['drink'] += ", "
        print("Drinks: " + request.session['drink'])
        request.session['comment'] = request.POST['comment']

        #Iterate through context dictionary
        #   Remove whitespace from beginning and end.
        #   Replace underscores with a space. 
        #   Capitalize the beginnings
        for key, value in request.session.items():
            if key not in ('csrfmiddlewaretoken', 'comment'):
                request.session[key] = value.strip().title().replace("_", " ")

    return redirect('/redirect')

def result_redirect(request):
    return render(request, 'result.html')