# Generated by Django 2.2.5 on 2019-11-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191104_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar/%Y%m%d/'),
        ),
    ]
