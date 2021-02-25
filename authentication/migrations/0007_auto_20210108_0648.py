# Generated by Django 3.1.4 on 2021-01-08 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20210107_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('job', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('bio', models.CharField(max_length=120)),
                ('skills', models.TextField()),
                ('work_title', models.CharField(max_length=255)),
                ('work_description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileFeedItem',
        ),
    ]
