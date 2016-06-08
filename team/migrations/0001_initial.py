# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('team_name', models.CharField(unique=True, max_length=120)),
                ('event', models.ForeignKey(related_name='event_team', max_length=120, to='events.Event')),
                ('team_lead', models.ForeignKey(related_name='team_leader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Members',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('members', models.ForeignKey(related_name='team_members', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(related_name='members', to='team.Team')),
            ],
        ),
    ]
