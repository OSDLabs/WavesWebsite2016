# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpmessage',
            name='messageDateTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='helpmessage',
            name='reply',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='helpmessage',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='helpmessage',
            name='message',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
