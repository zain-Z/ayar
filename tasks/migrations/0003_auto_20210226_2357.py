# Generated by Django 3.1 on 2021-02-26 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_auto_20210226_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomUser', to=settings.AUTH_USER_MODEL),
        ),
    ]