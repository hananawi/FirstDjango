# Generated by Django 2.2.5 on 2019-11-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20191107_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
