# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0013_auto_20160114_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='proglang',
            name='sort_id',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='projectbase',
            name='sort_id',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='randomstuff',
            name='sort_id',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='softskills',
            name='sort_id',
            field=models.IntegerField(default=99),
        ),
    ]
