# Generated by Django 3.2.4 on 2021-06-13 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_alter_store_favourites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='favourites',
            new_name='favourited_by',
        ),
    ]