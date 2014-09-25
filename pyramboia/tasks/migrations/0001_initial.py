# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arguments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('argument', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Headers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenttype', models.CharField(max_length=50)),
                ('charset', models.CharField(max_length=50)),
                ('soapaction', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response', models.TextField()),
                ('time', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('added_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=500)),
                ('name', models.ForeignKey(to='tasks.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=100)),
                ('request', models.TextField(max_length=1000, verbose_name=b'XML request')),
                ('threshold', models.FloatField()),
                ('test', models.CharField(max_length=100)),
                ('steps', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('arguments', models.ForeignKey(to='tasks.Arguments')),
                ('headers', models.ForeignKey(to='tasks.Headers')),
                ('project_name', models.ForeignKey(to='tasks.Project')),
                ('requires', models.ForeignKey(blank=True, to='tasks.Tasks', null=True)),
                ('target', models.ForeignKey(to='tasks.Target')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='history',
            name='project_name',
            field=models.ForeignKey(to='tasks.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='history',
            name='task_name',
            field=models.ForeignKey(to='tasks.Tasks'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='headers',
            name='name',
            field=models.ForeignKey(to='tasks.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arguments',
            name='name',
            field=models.ForeignKey(to='tasks.Project'),
            preserve_default=True,
        ),
    ]
