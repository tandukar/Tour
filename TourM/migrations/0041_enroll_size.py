# Generated by Django 3.2.8 on 2022-05-09 23:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0040_auto_20220509_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll',
            name='Size',
            field=models.PositiveIntegerField(default='1', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
