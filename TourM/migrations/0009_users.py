# Generated by Django 4.0.3 on 2022-04-18 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0008_remove_post_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
