# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0009_proglang_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='softskills',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
