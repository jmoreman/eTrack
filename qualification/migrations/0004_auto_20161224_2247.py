# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0003_auto_20161224_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathway',
            name='name',
            field=models.CharField(default='N/A', help_text='If the qualification has only one unnamed pathway, leave this field as N/A.', max_length=50),
        ),
    ]