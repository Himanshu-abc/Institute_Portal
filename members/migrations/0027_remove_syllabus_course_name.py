# Generated by Django 3.2.6 on 2021-09-15 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0026_alter_syllabus_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabus',
            name='course_name',
        ),
    ]
