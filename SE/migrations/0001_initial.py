# Generated by Django 2.1 on 2018-09-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dianliang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('dianliang', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='dianliu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('dianliu', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='dianya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('dianya', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='gonglv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('gonglv', models.CharField(max_length=32)),
            ],
        ),
    ]
