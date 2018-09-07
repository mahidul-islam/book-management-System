# Generated by Django 2.0.4 on 2018-08-30 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0006_book_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pic',
            new_name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='mark',
            field=models.BooleanField(default=False),
        ),
    ]