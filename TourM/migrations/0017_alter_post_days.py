# Generated by Django 4.0.3 on 2022-04-27 01:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0016_alter_post_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='days',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)]),
        ),
    ]
