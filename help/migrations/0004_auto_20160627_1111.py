# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_auto_20160614_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpmessage',
            name='reply',
            field=models.CharField(default=b'Waiting.......', max_length=5000),
        ),
    ]
