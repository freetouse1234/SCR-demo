# Generated by Django 5.0.4 on 2024-11-20 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboard', '0004_studentsignin_department_model_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsignin',
            name='image_model',
        ),
    ]