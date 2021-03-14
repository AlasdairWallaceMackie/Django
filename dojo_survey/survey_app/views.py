from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    context = {
        'name': None,
        'location': None,
        'language': None,
        'gender': None,
        'drink': "",
        'comment': None
    }

    if request.method=="POST":
        context['name'] = request.POST['name']
        context['location'] = request.POST['location']
        context['language'] = request.POST['language']

        if request.POST['gender'] == "prefer_not_to_say":
            context['gender'] = "Prefer Not to Say"
        else:
            context['gender'] = request.POST['gender']

        drink_list = request.POST.getlist('drink')
        for i in range ( len(drink_list) ):
            context['drink'] += drink_list[i]
            if i != len(drink_list)-1:
                context['drink'] += ", "

        context['comment'] = request.POST['comment']

        #Iterate through context dictionary
        #   Remove whitespace from beginning and end.
        #   Replace underscores with a space. 
        #   Capitalize the beginnings
        for key, value in context.items():
            if key not in ('csrfmiddlewaretoken', 'comment'):
                context[key] = value.strip().title().replace("_", " ")

    return render(request, 'result.html', context)
