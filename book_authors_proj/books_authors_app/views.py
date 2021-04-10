from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
import inspect

def index(request):
    return redirect("/books")

def add_object_page(request):
    print("Rendering add_object_page")
    current_class = request.get_full_path()[1:]
    cols = 30
    rows = 10

    print("Current_class: " + current_class)

    if current_class == 'books' or current_class == "":
        context = {
            'header': 'Add a Book',
            'form_fields':
                f"""<label for="title">Title<span class="star">*</span></label>
                <input required type="text" id="title" name="title">
                <br>
                <label for="description">Description<span class="star">*</span></label>
                <textarea required name="description" id="description" cols="{cols}" rows="{rows}"></textarea>
                <input type="hidden" name="object_type" value="book">""",
            'table': Book.objects.all()
        }
    elif current_class == 'authors':
        context = {
            'header': 'Add an Author',
            'form_fields':
                f"""<label for="first_name">First Name<span class="star">*</span></label>
                <input required type="text" id="first_name" name="first_name">
                <br>
                <label for="last_name">Last Name<span class="star">*</span></label>
                <input required type="text" id="last_name" name="last_name">
                <br>
                <label for="notes">Notes<span class="star">*</span></label>
                <textarea required name="notes" id="notes" cols="{cols}" rows="{rows}"></textarea>
                <input type="hidden" name="object_type" value="author">""",
            'table': Author.objects.all()
        }
    else:
        return HttpResponse("<h1>Error 404</h1>")

    context['current_path'] = current_class

    return render(request, 'add_object_page.html', context)

def info_page(request, table, id):
    if table == 'books':
        book = Book.objects.get(id=id)
        context = {
            'object_type': "book",
            'header': book.title,
            'id': id,
            'text_header': "Description",
            'text': book.desc,
            'assoc_header': 'Author',
            'associations': book.authors.all(),
            'complete_assoc_list': Author.objects.all(),
        }
    elif table == 'authors':
        author = Author.objects.get(id=id)
        context = {
            'object_type': "author",
            'header': (author.first_name + " " + author.last_name),
            'id': id,
            'text_header': "Notes",
            'text': author.notes,
            'assoc_header': 'Book',
            'associations': author.books.all(),
            'complete_assoc_list': Book.objects.all(),
        }
    else:
        return HttpResponse("ERROR 404")
    
    return render(request, 'info_page.html', context)


def add_object(request):
    print("add_object method called")
    if request.method == 'POST':
        print("Adding object")
        if request.POST['object_type'] == "book":
            Book.objects.create(
                title = request.POST['title'],
                desc = request.POST['description'],
            )
            print("Book added to database")
        elif request.POST['object_type'] == "author":
            Author.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                notes = request.POST['notes'],
            )
            print("Author added to database")
        else:
            print("Unknown object type submitted to form")
            return redirect('/')
        # redirection = f"/{{request.POST['object_type']}}"
    return redirect(f"/{request.POST['object_type']}s")

def delete_object(request):
    print("delete_object method called")
    id = request.POST['object_id']

    if request.method == 'POST':
        if request.POST['object_type'] == 'books':
            obj_to_delete = Book.objects.get(id = id)
        elif request.POST['object_type'] == 'authors':
            obj_to_delete = Author.objects.get(id = id)
        else:
            print("Unknown object to delete")
            return redirect('/')
        obj_to_delete.delete()

    print("Object deleted, redirecting: ")
    print(request.POST['object_type'])
    return redirect(f"/{request.POST['object_type']}")

def attach_object(request):
    print("Attaching object")

    object_type = request.POST['object_type']
    print("Object_type: " + object_type)

    id = request.POST['object_id']
    print("ID: " + id)

    attach_id = request.POST['object_to_attach']
    print("Attach ID: " + attach_id)

    if object_type == "book":
        print("It's a book!")
        object_to_edit = Book.objects.get(id = id)
        object_to_edit.authors.add( Author.objects.get(id = attach_id) )
    elif object_type == "author":
        print("It's an author!")
        object_to_edit = Author.objects.get(id = id)
        object_to_edit.books.add( Book.objects.get(id = attach_id) )
    else:
        print("Unknown object type")
        return redirect('/')

    object_to_edit.save()

    return redirect('/')