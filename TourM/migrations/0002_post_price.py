# Generated by Django 4.0.3 on 2022-04-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.CharField(default='', max_length=8),
        ),
    ]
