# Generated by Django 2.1.3 on 2019-04-15 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etherfeeds', '0027_auto_20190415_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashlist',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 23, 47, 8, 854046), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 23, 47, 8, 855571), verbose_name='date expiring'),
        ),
        migrations.AlterField(
            model_name='memberproposal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 15, 23, 47, 8, 855524), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='exp_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 23, 47, 8, 854343), verbose_name='date expiring'),
        ),
    ]
