# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 16:07
from __future__ import unicode_literals

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20171208_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='parents',
            field=mptt.fields.TreeManyToManyField(related_name='_category_parents_+', to='products.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
