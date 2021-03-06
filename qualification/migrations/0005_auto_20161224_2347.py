# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0004_auto_20161224_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='glh',
            field=models.IntegerField(verbose_name='guided learning hours'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='level',
            field=models.IntegerField(choices=[(2, 'Level 2'), (3, 'Level 3')], default=3),
        ),
    ]
