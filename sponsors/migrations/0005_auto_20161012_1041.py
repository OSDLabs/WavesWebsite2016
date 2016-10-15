# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0004_auto_20161005_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='sponsCategory',
            field=models.CharField(default=b'', max_length=50, choices=[('Title Sponsor', 'Title Sponsor'), ('Media Partners', 'Media Partners'), ('Event Partners', 'Event Partners'), ('Food and Beverages Partners', 'Food and Beverages Partners'), ('Ambience Partners', 'Ambiance Partners')]),
        ),
    ]
