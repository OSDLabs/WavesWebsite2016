# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wavesprofile', '0007_auto_20160606_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x430', help_text=None, hide_image_field=False, verbose_name='cropping', size_warning=False, adapt_rotation=False, allow_fullsize=False, free_crop=False),
        ),
    ]
