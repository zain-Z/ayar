# Generated by Django 3.1 on 2021-03-13 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20210313_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.work'),
        ),
    ]
