# Generated by Django 3.2.4 on 2021-06-13 12:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0003_remove_store_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
