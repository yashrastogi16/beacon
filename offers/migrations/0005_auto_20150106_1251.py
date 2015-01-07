# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_offer_min_stay_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='min_stay_time',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
