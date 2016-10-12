# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_sponsor_sponspic'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='sponsURL',
            field=models.URLField(default='lite'),
        ),
    ]
