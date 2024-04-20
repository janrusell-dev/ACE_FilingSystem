# Generated by Django 4.2.2 on 2024-04-16 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0008_remove_addfacultydocument_upload_files_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStaffDocImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='scans/')),
                ('staff_doc', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file_app.addstaffdocument')),
            ],
        ),
    ]
