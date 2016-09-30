# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20160625_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_category',
            field=models.CharField(default='', choices=[('Drama', 'Drama'), ('Dance', 'Dance'), ('Big 4', 'Big 4'), ('Business', 'Business'), ('Fine Arts', 'Fine Arts'), ('Literary', 'Literary'), ('Music', 'Music'), ('Film and Photography', 'Film and Photography'), ('Quiz', 'Quiz'), ('Special', 'Special')], max_length=50),
        ),
    ]
