# Generated by Django 4.0.3 on 2022-04-27 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0018_alter_post_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Provinces',
            field=models.CharField(max_length=255),
        ),
    ]
