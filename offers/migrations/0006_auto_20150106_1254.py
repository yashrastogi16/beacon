# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_auto_20150106_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='min_stay_time',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
