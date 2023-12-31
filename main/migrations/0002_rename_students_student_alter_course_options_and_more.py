# Generated by Django 4.2.6 on 2023-10-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '3. Courses'},
        ),
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name_plural': '2. CourseCategories'},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name_plural': '1. Instructors'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '4. Students'},
        ),
        migrations.AlterField(
            model_name='instructor',
            name='qualification',
            field=models.CharField(choices=[('BSC', 'Bachelor of Science'), ('MSC', 'Master'), ('BA', 'Bachelor of Arts'), ('NCE', 'National Certificate Examination'), ('ND', 'National Diploma'), ('HND', 'Higher National Diploma')], max_length=5),
        ),
    ]
