# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lumos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'soft_skills',
            },
        ),
        migrations.CreateModel(
            name='SoftSkillsData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('difficulty', models.IntegerField(default=0, choices=[(0, b'Beginner'), (1, b'Intermediate'), (2, b'Advanced')])),
                ('diff_sort', models.IntegerField(default=99)),
                ('media_type', models.IntegerField(default=3, choices=[(0, b'Video'), (1, b'Article'), (2, b'Interactive Site'), (3, b'Other')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('soft_skill', models.ForeignKey(to='lumos.SoftSkills')),
            ],
            options={
                'db_table': 'soft_knowlege_base',
            },
        ),
        migrations.AlterField(
            model_name='knowledgebase',
            name='media_type',
            field=models.IntegerField(default=3, choices=[(0, b'Video'), (1, b'Article'), (2, b'Interactive Site'), (3, b'Other')]),
        ),
        migrations.AlterModelTable(
            name='knowledgebase',
            table='tech_knowlege_base',
        ),
    ]
