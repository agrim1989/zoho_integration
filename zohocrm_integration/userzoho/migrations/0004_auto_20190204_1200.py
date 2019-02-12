# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-02-04 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userzoho', '0003_subtasks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subtasks',
            options={'ordering': ('-created_at',), 'verbose_name': 'Sub Tasks', 'verbose_name_plural': 'Sub Tasks'},
        ),
        migrations.AlterField(
            model_name='subtasks',
            name='created_person',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
