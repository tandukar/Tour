# Generated by Django 4.0.3 on 2022-04-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0005_alter_post_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pack_img',
            field=models.ImageField(blank=True, null=True, upload_to='pacImages/'),
        ),
    ]
