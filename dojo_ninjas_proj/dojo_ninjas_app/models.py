from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField

class Dojo(models.Model):
    name = CharField(max_length=255)
    city = CharField(max_length=255)
    state = CharField(max_length=2)
    #ninjas (class Ninja)
    desc = TextField(default="Old Dojo")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Dojo id({self.id}): {self.name} in {self.city}, {self.state}>"

class Ninja(models.Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Ninja id({self.id}): {self.first_name} {self.last_name} of Dojo: {self.dojo.name}>"

