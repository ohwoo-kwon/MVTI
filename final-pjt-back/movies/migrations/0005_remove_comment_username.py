# Generated by Django 3.2.3 on 2021-05-21 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_comment_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
    ]
