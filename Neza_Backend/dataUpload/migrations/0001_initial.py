# Generated by Django 4.2.5 on 2023-09-07 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_type', models.CharField(max_length=50)),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_upload_status', models.CharField(max_length=20)),
            ],
        ),
    ]