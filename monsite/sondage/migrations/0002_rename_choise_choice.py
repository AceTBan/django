# Generated by Django 3.2.12 on 2022-03-17 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sondage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choise',
            new_name='Choice',
        ),
    ]
