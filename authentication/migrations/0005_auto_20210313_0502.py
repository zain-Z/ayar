# Generated by Django 3.1 on 2021-03-13 03:02

import authentication.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210307_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(blank=True, default=' ', max_length=255, null=True)),
                ('work_description', models.TextField(blank=True, default='', null=True)),
                ('work_url', models.CharField(blank=True, max_length=255, null=True)),
                ('work_date', models.DateField(blank=True, null=True)),
                ('work_skills', models.TextField(blank=True, default='', null=True)),
                ('upload_work_files', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_one', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_two', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_three', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_four', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_five', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_six', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_seven', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_eight', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_nine', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_ten', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_eleven', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('upload_work_files_twelve', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_eight',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_eleven',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_five',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_four',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_nine',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_one',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_seven',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_six',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_ten',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_three',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_twelve',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upload_work_files_two',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work_description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work_skills',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work_title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='work_url',
        ),
        migrations.AddField(
            model_name='user',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.work'),
        ),
    ]