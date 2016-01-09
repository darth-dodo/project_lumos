# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0010_softskills_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proglang',
            name='name',
            field=models.CharField(max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='softskills',
            name='name',
            field=models.CharField(max_length=100, unique=True, null=True),
        ),
    ]
