# Generated by Django 3.1 on 2020-11-29 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aljoadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AljoadminComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aljoadmin.aljoadmin')),
                ('wirter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modify_dt'],
            },
        ),
    ]
