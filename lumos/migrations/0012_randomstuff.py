# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0011_auto_20160109_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomStuff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('media_type', models.IntegerField(default=3, choices=[(0, b'Video'), (1, b'Article'), (2, b'Interactive Site'), (3, b'Other')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'random_stuff',
            },
        ),
    ]
