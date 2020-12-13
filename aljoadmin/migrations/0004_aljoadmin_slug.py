# Generated by Django 3.1 on 2020-11-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aljoadmin', '0003_delete_aljoadmincomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='aljoadmin',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='one word for title alias.', null=True, unique=True, verbose_name='SLUG'),
        ),
    ]
