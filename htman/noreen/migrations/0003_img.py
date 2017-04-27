# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0002_auto_20151227_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('IMG_pk', models.AutoField(max_length=255, serialize=False, primary_key=True)),
                ('pwd', models.CharField(max_length=255)),
                ('article', models.CharField(default=b'', max_length=255)),
            ],
        ),
    ]
