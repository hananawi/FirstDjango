# Generated by Django 2.2.5 on 2019-11-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]