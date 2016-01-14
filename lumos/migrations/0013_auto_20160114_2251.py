# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0012_randomstuff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledgebase',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectbase',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='randomstuff',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='softskillsdata',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userfeedback',
            name='feedback_note',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userfeedback',
            name='username',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
