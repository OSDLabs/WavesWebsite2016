# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesprofile', '0003_auto_20160530_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pic',
        ),
    ]
