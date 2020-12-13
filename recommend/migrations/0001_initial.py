# Generated by Django 3.1 on 2020-12-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('q1', models.IntegerField(null=True)),
                ('q2', models.IntegerField(null=True)),
                ('q3', models.IntegerField(null=True)),
                ('q4', models.IntegerField(null=True)),
                ('q5', models.IntegerField(null=True)),
                ('q6', models.IntegerField(null=True)),
                ('q7', models.IntegerField(null=True)),
                ('q8', models.IntegerField(null=True)),
                ('q9', models.IntegerField(null=True)),
                ('q10', models.IntegerField(null=True)),
                ('q11', models.IntegerField(null=True)),
                ('q12', models.IntegerField(null=True)),
                ('q13', models.IntegerField(null=True)),
                ('q14', models.IntegerField(null=True)),
                ('q15', models.IntegerField(null=True)),
                ('q16', models.IntegerField(null=True)),
                ('q17', models.IntegerField(null=True)),
                ('q18', models.IntegerField(null=True)),
                ('q19', models.IntegerField(null=True)),
                ('q20', models.IntegerField(null=True)),
            ],
        ),
    ]
