# Generated by Django 2.1 on 2019-01-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0012_news_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
