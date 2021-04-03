from django.shortcuts import redirect, render
from .models import *
from django.db.models import Count

def index(request):
    print("INDEX CALLED")
    
    all_dojos = Dojo.objects.all()
    all_dojos = Dojo.objects.annotate( number_of_ninjas = Count('ninjas') )

    context = {
        'all_dojos': all_dojos
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    # TODO: Check for duplicate dojo names
    if request.method == 'POST':
        Dojo.objects.create(
            name = request.POST['dojo_name'],
            city = request.POST['dojo_city'],
            state = request.POST['dojo_state']
            )
    return redirect('/')

def add_ninja(request):
    if request.method == 'POST':
        Ninja.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            dojo = Dojo.objects.get(name = request.POST['dojo_select'])
            )
    return redirect('/')

def delete(request):
    if request.method == "POST":
        dojo_name = request.POST['dojo_to_delete']
        print("Dojo to delete: " + dojo_name)
        dojo_to_delete = Dojo.objects.get(name = dojo_name)
        dojo_to_delete.delete()
        print(f"Dojo Object: {dojo_name} DELETED")

    return redirect('/')

def get_dojos(request):
    print("Get_Dojos called")
    return Dojo.objects.all()
