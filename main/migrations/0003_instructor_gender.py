# Generated by Django 4.2.6 on 2023-10-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_students_student_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='none', max_length=5),
        ),
    ]
