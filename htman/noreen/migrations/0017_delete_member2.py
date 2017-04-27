# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0016_member2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member2',
        ),
    ]
