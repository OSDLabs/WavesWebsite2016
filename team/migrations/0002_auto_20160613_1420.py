# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_lead',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='team_lead'),
        ),
        migrations.AlterField(
            model_name='team_members',
            name='members',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, related_name='team_members'),
        ),
        migrations.AlterField(
            model_name='team_members',
            name='team',
            field=models.ForeignKey(to='team.Team', related_name='team'),
        ),
    ]
