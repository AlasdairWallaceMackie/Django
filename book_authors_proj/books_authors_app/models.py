from typing import Text
from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ManyToManyField

class Book(models.Model):
    title = CharField(max_length=255)
    desc = TextField()
    ## authors (many to many relationship w/ Author)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Book id ({self.id}): {self.title} by {self.authors.all()}>"

    def get_full_name(self):
        return self.title

    def class_name(self):
        return self.__class__.__name__

    def get_assoc_name(self):
        return 'authors'

class Author(models.Model):
    first_name = CharField(max_length=45)
    last_name = CharField(max_length=45)
    notes = TextField(default="Author notes here")
    books = ManyToManyField(Book, related_name="authors")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Author id ({self.id}): {self.first_name} {self.last_name}>"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def class_name(self):
        return self.__class__.__name__

    def get_assoc_name(self):
        return 'books'