# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0005_target_ve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='ve',
        ),
    ]