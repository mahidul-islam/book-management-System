# Generated by Django 2.0.4 on 2018-08-29 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookowner',
            old_name='addr',
            new_name='address',
        ),
    ]
