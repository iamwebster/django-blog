# Generated by Django 4.2.7 on 2023-11-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yapp', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
