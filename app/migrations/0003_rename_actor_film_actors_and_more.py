# Generated by Django 4.2.4 on 2023-08-24 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_film_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='actor',
            new_name='actors',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='produser',
            new_name='producer',
        ),
    ]
