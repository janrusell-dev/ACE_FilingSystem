# Generated by Django 4.2.2 on 2024-04-25 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0014_sfdocument_sffile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sffile',
            name='staff_docs',
        ),
        migrations.DeleteModel(
            name='SfDocument',
        ),
        migrations.DeleteModel(
            name='SfFile',
        ),
    ]
