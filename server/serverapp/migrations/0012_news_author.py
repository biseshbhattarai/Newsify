# Generated by Django 2.1 on 2019-01-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverapp', '0011_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
    ]