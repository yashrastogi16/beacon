# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import offers.models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='entry_exit_type',
            field=models.CharField(max_length=50, choices=[(b'1', b'Entry'), (b'0', b'Exit')]),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_code',
            field=models.CharField(default=offers.models.number, max_length=50),
        ),
    ]
