# Generated by Django 4.2.5 on 2023-09-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_dashboard_no_of_industries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='no_of_industries',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
