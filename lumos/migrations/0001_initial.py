# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('difficulty', models.IntegerField(choices=[(0, b'Beginner'), (1, b'Intermediate'), (2, b'Advanced')])),
                ('diff_sort', models.IntegerField(default=99)),
                ('media_type', models.IntegerField(choices=[(0, b'Video'), (1, b'Article'), (2, b'Interative Site')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'knw_base',
            },
        ),
        migrations.CreateModel(
            name='ProgLang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=20, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'prog_lang',
            },
        ),
        migrations.AddField(
            model_name='knowledgebase',
            name='prog_lang',
            field=models.ForeignKey(to='lumos.ProgLang'),
        ),
    ]
