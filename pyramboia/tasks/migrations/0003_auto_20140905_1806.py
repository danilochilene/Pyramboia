# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20140902_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='arguments',
            field=models.ForeignKey(blank=True, to='tasks.Argument', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='test',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
