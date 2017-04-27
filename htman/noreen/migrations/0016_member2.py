# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0015_auto_20151229_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member2',
            fields=[
                ('member_pk', models.AutoField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('member_img', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
