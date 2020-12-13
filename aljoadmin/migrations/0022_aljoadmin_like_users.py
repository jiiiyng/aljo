# Generated by Django 3.1 on 2020-12-01 14:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aljoadmin', '0021_remove_aljoadmin_likes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='aljoadmin',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
