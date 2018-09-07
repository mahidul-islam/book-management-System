# Generated by Django 2.0.4 on 2018-09-01 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
