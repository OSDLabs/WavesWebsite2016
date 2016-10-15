# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sponsName', models.CharField(max_length=100)),
                ('sponsCategory', models.CharField(max_length=50, choices=[('Title Sponsor', 'Title Sponsor'), ('Media Partners', 'Media Partners'), ('Event Partners', 'Event Partners'), ('Food and Beverages Partners', 'Food and Beverages Partners'), ('Ambiance Partners', 'Ambiance Partners')], default='')),
            ],
        ),
    ]
