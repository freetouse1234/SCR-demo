# Generated by Django 5.0.4 on 2024-11-20 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentsignin',
            options={},
        ),
        migrations.AlterModelManagers(
            name='studentsignin',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='studentsignin',
            name='username',
        ),
    ]
