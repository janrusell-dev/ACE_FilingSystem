# Generated by Django 4.2.2 on 2024-04-08 01:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0003_addfacultydocument_subject_addstaffdocument_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfacultydocument',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='addstaffdocument',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]