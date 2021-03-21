from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import random, datetime


def index(request):
    print("HOMEPAGE")
    if request.session.has_key('gold') == False:
        request.session['gold'] = 0

    if request.session.has_key('activity_list') == False:
        print('dict initialized')
        request.session['activity_list'] = []
        request.session['activity_text'] = ""
    else:
        request.session['activity_text'] = ""
        for i in range( len(request.session['activity_list']) ):
            request.session['activity_text'] += (request.session['activity_list'][i] + "\r")
    return render(request, 'index.html')

def process_money(request):
    
    location = request.POST['location']
    if location == 'farm':
        added_gold = random.randrange(10,20)
    elif location == 'cave':
        added_gold = random.randrange(5,10)
    elif location == 'house':
        added_gold = random.randrange(2,5)
    elif location == 'casino':
        added_gold = random.randrange(-50,50)

    current_datetime = datetime.datetime.now()
    current_datetime = current_datetime.strftime("(%b %d, %Y %I:%M %p)")

    if added_gold > 0:
        request.session['activity_list'].insert(0, f"<span style='color: green'>Earned {added_gold} gold from the {location} {current_datetime}</span><br>")
    elif added_gold < 0:
        request.session['activity_list'].insert(0, f"<span style='color: red'>Entered the {location} and lost {added_gold} gold....whoopsie {current_datetime}</span><br>")
    elif added_gold == 0:
        request.session['activity_list'].insert(0, f"<span style='color: orange'>Went to the {location}, but didn't lose or earn any gold {current_datetime}</span><br>")

    print(f"DATE AND TIME: {current_datetime}")

    request.session['gold']+=added_gold
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity_text'] = ""
    request.session['activity_list'] = []
    return redirect('/')