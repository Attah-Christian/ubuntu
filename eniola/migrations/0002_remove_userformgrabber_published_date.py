# Generated by Django 5.0 on 2023-12-23 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eniola', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userformgrabber',
            name='published_date',
        ),
    ]
