# Generated by Django 2.2.5 on 2019-11-17 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
