# Generated by Django 2.0.4 on 2018-08-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0005_auto_20180830_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Spirituality', 'Spirituality'), ('Tafseer', 'Tafseer'), ('Hadith', 'Hadith'), ('Aqeedah', 'Aqeedah')], default='Spirituality', max_length=32),
        ),
    ]
