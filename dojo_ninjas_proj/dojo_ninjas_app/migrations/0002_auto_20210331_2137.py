# Generated by Django 2.2 on 2021-03-31 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]
