# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-29 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='labels',
            field=models.CharField(default='default', max_length=400),
            preserve_default=False,
        ),
    ]
