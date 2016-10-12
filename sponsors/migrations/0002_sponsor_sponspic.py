# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='sponsPic',
            field=models.ImageField(null=True, blank=True, upload_to='adminuploads/sponsors/pics'),
        ),
    ]
