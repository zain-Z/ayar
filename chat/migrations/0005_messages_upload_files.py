# Generated by Django 3.1.4 on 2021-01-20 20:48

import chat.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210120_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='upload_files',
            field=models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[chat.validators.validate_file_extension, chat.validators.validate_image_extension]),
        ),
    ]
