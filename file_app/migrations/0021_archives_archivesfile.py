# Generated by Django 4.2.2 on 2024-04-26 13:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0020_delete_facultydocs_delete_fileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.campus')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file_app.department')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='ArchivesFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='archives')),
                ('archives', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='file_app.archives')),
            ],
        ),
    ]
