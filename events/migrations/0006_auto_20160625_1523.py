# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_category',
            field=models.CharField(choices=[('Drama', 'Drama'), ('Dance', 'Dance'), ('Big4', 'Big4'), ('Business', 'Business'), ('Fine Arts', 'Fine Arts'), ('Literary', 'Literary'), ('Music', 'Music'), ('Film', 'Film'), ('Photography', 'Photography'), ('Quiz', 'Quiz'), ('Special', 'Special')], default='', max_length=50),
        ),
    ]
