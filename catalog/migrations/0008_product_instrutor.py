# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20160805_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='instrutor',
            field=models.CharField(default='A', max_length=50, verbose_name='Instrutor'),
            preserve_default=False,
        ),
    ]
