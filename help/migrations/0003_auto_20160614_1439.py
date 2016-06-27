# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0002_auto_20160614_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpmessage',
            name='reply',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
