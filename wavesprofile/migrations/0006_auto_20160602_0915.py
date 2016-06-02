# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wavesprofile', '0005_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(max_length=2, choices=[('U1', 'Undergraduate 1st year'), ('U2', 'Undergraduate 2nd year'), ('U3', 'Undergraduate 3rd year'), ('U4', 'Undergraduate 4th year'), ('P1', 'Postgraduate 1st year'), ('P2', 'Postgraduate 2nd year'), ('SS', 'Schooling'), ('PH', 'PhD.')]),
        ),
    ]
