# Generated by Django 3.2.6 on 2021-09-15 04:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0021_rename_courses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='semester',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
