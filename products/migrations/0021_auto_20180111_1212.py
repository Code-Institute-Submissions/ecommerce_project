# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20171220_1151'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('parent', 'slug')]),
        ),
    ]
