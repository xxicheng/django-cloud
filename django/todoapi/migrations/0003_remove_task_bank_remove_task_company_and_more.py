# Generated by Django 4.0.dev20210628094637 on 2021-08-16 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0002_alter_task_bank_alter_task_company_alter_task_month_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='task',
            name='company',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project_country',
        ),
    ]
