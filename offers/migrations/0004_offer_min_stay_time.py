# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_auto_20150106_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='min_stay_time',
            field=models.CharField(default=b'30 mins', max_length=20),
            preserve_default=True,
        ),
    ]
