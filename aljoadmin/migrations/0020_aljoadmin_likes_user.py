# Generated by Django 3.1 on 2020-12-01 12:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aljoadmin', '0019_aljoadmin_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='aljoadmin',
            name='likes_user',
            field=models.ManyToManyField(blank=True, related_name='likes_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
