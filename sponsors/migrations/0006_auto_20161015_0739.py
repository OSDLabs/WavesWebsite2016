# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0005_auto_20161012_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='sponsURL',
            field=models.URLField(blank=True),
        ),
    ]
