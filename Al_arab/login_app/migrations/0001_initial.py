# Generated by Django 3.1.7 on 2021-03-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('mob_number', models.IntegerField(unique=True, verbose_name='Mobile Number')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
