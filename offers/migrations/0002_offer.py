# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon_info', '__first__'),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offer_code', models.CharField(max_length=50)),
                ('entry_exit_type', models.CharField(max_length=50, null=True)),
                ('offername', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('membership', models.CharField(default=1, max_length=5)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('store_code', models.ForeignKey(to='beacon_info.store')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
