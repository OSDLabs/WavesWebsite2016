# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_sponsor_sponsurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='sponsURL',
            field=models.URLField(default="add sponsor's webpage"),
        ),
    ]
