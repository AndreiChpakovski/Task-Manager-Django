# Generated by Django 4.2.13 on 2024-06-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_task_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]
