# Generated by Django 3.1 on 2021-03-12 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersskill',
            old_name='owner',
            new_name='user',
        ),
    ]
