# Generated by Django 3.1.4 on 2021-01-20 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20210120_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default='', max_length=10)),
                ('description', models.TextField()),
                ('date', models.DateField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='offer',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='chat.offer'),
        ),
    ]