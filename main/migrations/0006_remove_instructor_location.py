# Generated by Django 4.2.6 on 2023-10-22 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_locations_instructor_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='location',
        ),
    ]
