# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesprofile', '0004_remove_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.FileField(upload_to='uploads/', default=''),
        ),
    ]
