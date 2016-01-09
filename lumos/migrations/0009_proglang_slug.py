# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0008_userfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='proglang',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
