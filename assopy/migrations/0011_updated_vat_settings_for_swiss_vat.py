# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assopy', '0010_add_uuid_to_Order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
