# Generated by Django 3.2.3 on 2021-07-18 07:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0004_auto_20210718_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 7, 4, 7, 742628, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 7, 4, 7, 742628, tzinfo=utc)),
        ),
    ]
