# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_pk', models.AutoField(max_length=255, serialize=False, primary_key=True)),
                ('member_name', models.CharField(default=b'', max_length=255)),
                ('member_rank', models.IntegerField(default=0)),
                ('value_1', models.IntegerField(default=0)),
                ('value_2', models.IntegerField(default=0)),
                ('value_3', models.IntegerField(default=0)),
                ('value_4', models.IntegerField(default=0)),
                ('value_5', models.IntegerField(default=0)),
                ('value_6', models.IntegerField(default=0)),
                ('value_7', models.IntegerField(default=0)),
                ('value_8', models.IntegerField(default=0)),
                ('value_9', models.IntegerField(default=0)),
                ('value_10', models.IntegerField(default=0)),
                ('value_11', models.IntegerField(default=0)),
                ('value_12', models.IntegerField(default=0)),
                ('value_13', models.IntegerField(default=0)),
                ('value_14', models.IntegerField(default=0)),
                ('value_15', models.IntegerField(default=0)),
                ('value_16', models.IntegerField(default=0)),
                ('value_17', models.IntegerField(default=0)),
                ('value_18', models.IntegerField(default=0)),
                ('value_19', models.IntegerField(default=0)),
                ('value_20', models.IntegerField(default=0)),
                ('value_21', models.IntegerField(default=0)),
                ('value_22', models.IntegerField(default=0)),
                ('value_23', models.IntegerField(default=0)),
                ('value_24', models.IntegerField(default=0)),
                ('value_25', models.IntegerField(default=0)),
                ('value_26', models.IntegerField(default=0)),
                ('value_27', models.IntegerField(default=0)),
                ('value_28', models.IntegerField(default=0)),
                ('value_29', models.IntegerField(default=0)),
                ('value_30', models.IntegerField(default=0)),
                ('value_sum', models.IntegerField(default=0)),
                ('test_result', models.CharField(default=b'', max_length=255)),
                ('level_result', models.CharField(default=b'', max_length=255)),
                ('test_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
