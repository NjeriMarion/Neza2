# Generated by Django 4.2.5 on 2023-09-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagetracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationstagetracking',
            name='stage_name',
            field=models.CharField(choices=[('Planning', 'Planning'), ('Testing', 'Testing'), ('Treating', 'Treating')], max_length=255),
        ),
    ]
