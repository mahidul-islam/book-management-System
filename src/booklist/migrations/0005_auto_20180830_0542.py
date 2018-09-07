# Generated by Django 2.0.4 on 2018-08-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0004_auto_20180829_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('BANGLA', 'Bangla'), ('ENGLISH', 'English'), ('ARABIC', 'Arabic'), ('URDU', 'Urdu')], default='BANGLA', max_length=32),
        ),
    ]
