# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160607_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indi_event_participants',
            name='event',
            field=models.ForeignKey(related_name='event', to='events.Event'),
        ),
    ]
