# Generated by Django 3.2.8 on 2022-05-08 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0035_rename_enrol_enroll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='post',
        ),
    ]
