# Generated by Django 3.1 on 2020-12-12 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0008_auto_20201213_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommend',
            name='user',
        ),
    ]