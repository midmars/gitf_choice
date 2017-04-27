# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0010_auto_20151228_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='article',
            field=models.TextField(),
        ),
    ]
