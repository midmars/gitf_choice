# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0011_auto_20151228_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='MQV',
            fields=[
                ('MQV_pk', models.AutoField(max_length=255, serialize=False, primary_key=True)),
                ('qn', models.IntegerField()),
                ('member_pk', models.IntegerField()),
                ('value', models.IntegerField(default=-1)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_1',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_10',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_11',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_12',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_13',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_14',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_15',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_16',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_17',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_18',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_19',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_2',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_20',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_21',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_22',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_23',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_24',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_25',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_26',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_27',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_28',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_29',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_3',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_30',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_4',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_5',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_6',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_7',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_8',
        ),
        migrations.RemoveField(
            model_name='member',
            name='value_9',
        ),
    ]
