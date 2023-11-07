# Generated by Django 4.2.6 on 2023-10-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_instructor_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_covered', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='location_covered',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='instructor',
            name='locations',
            field=models.ManyToManyField(blank=True, default='', null=True, to='main.routes'),
        ),
    ]
