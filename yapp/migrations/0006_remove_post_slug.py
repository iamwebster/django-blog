# Generated by Django 4.2.7 on 2023-11-10 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yapp', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
