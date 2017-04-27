# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noreen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QAE',
            fields=[
                ('explain_pk', models.AutoField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_pk', models.AutoField(max_length=255, serialize=False, primary_key=True)),
                ('number', models.IntegerField()),
                ('article', models.CharField(max_length=255)),
                ('attribute', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='finsh',
            field=models.IntegerField(default=0),
        ),
    ]
