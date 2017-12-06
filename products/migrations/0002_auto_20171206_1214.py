# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='aw_image_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='search_price',
        ),
        migrations.AddField(
            model_name='product',
            name='aw_deep_link',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='merchant_category',
            field=models.CharField(default='', max_length=500),
        ),
    ]
