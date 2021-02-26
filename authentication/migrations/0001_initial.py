# Generated by Django 3.1 on 2021-02-26 21:48

import authentication.validators
import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('language', models.CharField(choices=[('ARABIC', 'ARABIC'), ('ENGLISH', 'ENGLISH')], default='ARABIC', max_length=255)),
                ('user_type', models.CharField(choices=[('Developer', 'Developer'), ('Customer', 'Customer')], default='Developer', max_length=30)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('country_code', models.CharField(blank=True, choices=[('SAUDIARABIA', '+966'), ('JORDAN', '+962'), ('UNITEDARABEMIRATES', '+971'), ('BAHRAIN', '+973'), ('IRAQ', '+964')], default='SAUDIARABIA', max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, default='', max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.             Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('job', models.CharField(db_index=True, default=' ', max_length=255)),
                ('skills', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_image_extension])),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_image_extension])),
                ('about_me', models.TextField(blank=True, null=True)),
                ('work_title', models.CharField(blank=True, default=' ', max_length=255, null=True)),
                ('work_description', models.TextField(blank=True, default='', null=True)),
                ('work_url', models.CharField(blank=True, max_length=255, null=True)),
                ('work_date', models.DateField(blank=True, null=True)),
                ('work_skills', models.TextField(blank=True, default='', null=True)),
                ('upload_work_files', models.FileField(blank=True, null=True, upload_to='uploaded_files/', validators=[authentication.validators.validate_file_extension])),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth_provider', models.CharField(default='email', max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
