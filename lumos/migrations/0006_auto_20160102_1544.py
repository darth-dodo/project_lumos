# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0005_auto_20160102_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectbase',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
