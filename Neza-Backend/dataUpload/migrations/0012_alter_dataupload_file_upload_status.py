# Generated by Django 4.2.5 on 2023-09-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataUpload', '0011_alter_dataupload_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataupload',
            name='file_upload_status',
            field=models.CharField(choices=[('Progress', 'progress'), ('uploaded', 'uploaded'), ('completed', 'completed')], max_length=16),
        ),
    ]
