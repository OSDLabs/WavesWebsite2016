# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20160625_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('roundTitle', models.CharField(max_length=50)),
                ('roundDay', models.DateField()),
                ('roundLocation', models.CharField(max_length=50)),
                ('roundTime', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='event_category',
            field=models.CharField(choices=[('Drama', 'Drama'), ('Dance', 'Dance'), ('Big 4', 'Big 4'), ('Business', 'Business'), ('Fine Arts', 'Fine Arts'), ('Literary', 'Literary'), ('Music', 'Music'), ('Film and Photography', 'Film and Photography'), ('Quiz', 'Quiz'), ('Special', 'Special')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='rounds',
            name='event',
            field=models.ForeignKey(related_name='rounds', to='events.Event'),
        ),
    ]
