# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesprofile', '0009_auto_20160606_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cropping',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
