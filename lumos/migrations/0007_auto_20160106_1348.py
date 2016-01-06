# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0006_auto_20160102_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='proglang',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='softskills',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
    ]
