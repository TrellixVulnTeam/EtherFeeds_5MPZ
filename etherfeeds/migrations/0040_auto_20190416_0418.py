# Generated by Django 2.1.3 on 2019-04-16 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etherfeeds', '0039_auto_20190416_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashlist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 4, 18, 24, 489821), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 4, 18, 24, 491394), verbose_name='date expiring'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 4, 18, 24, 491345), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 4, 18, 24, 490130), verbose_name='date expiring'),
        ),
    ]
