# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_catagory',
            field=models.CharField(max_length=50, default='', choices=[('Drama', 'Drama'), ('Dance', 'Dance'), ('Comedy', 'Comedy')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventRules',
            field=models.FileField(blank=True, upload_to='adminuploads/events/rules/', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventpic',
            field=models.ImageField(blank=True, upload_to='adminuploads/events/pics/', null=True),
        ),
    ]
