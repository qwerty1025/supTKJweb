# Generated by Django 3.1 on 2020-08-15 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamehub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='acc_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='acc_no',
        ),
    ]
