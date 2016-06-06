# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesprofile', '0006_auto_20160602_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=100)),
                ('eventDate', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(to='wavesprofile.Profile', to_field=b'user', null=True)),
            ],
        ),
    ]
