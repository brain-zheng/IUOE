# Generated by Django 2.1 on 2018-10-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SE', '0002_auto_20180930_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('e_mail', models.CharField(max_length=32)),
            ],
        ),
    ]
