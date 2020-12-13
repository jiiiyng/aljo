# Generated by Django 3.1 on 2020-11-30 12:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aljoadmin', '0016_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='aljoadmin',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
