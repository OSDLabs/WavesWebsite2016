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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=120)),
                ('pic', models.FileField(upload_to='uploads/')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('institute', models.CharField(max_length=120)),
                ('department', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=1)),
                ('dob', models.DateField()),
                ('year', models.CharField(max_length=2)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('settime', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
