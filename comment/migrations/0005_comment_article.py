# Generated by Django 2.2.5 on 2019-11-17 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20191107_2300'),
        ('comment', '0004_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='article.Article'),
        ),
    ]
