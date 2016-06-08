# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('eventName', models.CharField(max_length=100)),
                ('eventDate', models.DateTimeField(null=True)),
                ('eventRules', models.FileField(upload_to='adminuploads/events/rules/', null=True)),
                ('eventpic', models.ImageField(upload_to='adminuploads/events/pics/', null=True)),
                ('event_desc', models.TextField(null=True)),
                ('event_type', models.CharField(choices=[('T', 'Team'), ('S', 'Single')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Indi_Event_Participants',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('event', models.ForeignKey(to='events.Event', related_name='event_participants')),
                ('event_part', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='event_participating')),
            ],
        ),
    ]
