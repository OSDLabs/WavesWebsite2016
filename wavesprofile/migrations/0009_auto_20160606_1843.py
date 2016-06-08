# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesprofile', '0008_profile_cropping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pic',
            new_name='image',
        ),
    ]
