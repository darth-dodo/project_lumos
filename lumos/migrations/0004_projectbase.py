# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0003_auto_20160102_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('difficulty', models.IntegerField(default=0, choices=[(0, b'Beginner'), (1, b'Intermediate'), (2, b'Advanced')])),
                ('diff_sort', models.IntegerField(default=99)),
                ('media_type', models.IntegerField(default=3, choices=[(0, b'Video'), (1, b'Article'), (2, b'Interactive Site'), (3, b'Other')])),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('prog_lang', models.ManyToManyField(to='lumos.ProgLang')),
            ],
            options={
                'db_table': 'tech_project_base',
            },
        ),
    ]
