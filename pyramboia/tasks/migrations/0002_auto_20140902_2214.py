# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('argument', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=200)),
                ('name', models.ForeignKey(to='tasks.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenttype', models.CharField(max_length=50)),
                ('charset', models.CharField(max_length=50)),
                ('soapaction', models.CharField(max_length=100)),
                ('name', models.ForeignKey(to='tasks.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=100)),
                ('request', models.TextField(max_length=1000, verbose_name=b'XML request')),
                ('threshold', models.FloatField()),
                ('test', models.CharField(max_length=100)),
                ('steps', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('arguments', models.ForeignKey(to='tasks.Argument')),
                ('header', models.ForeignKey(to='tasks.Header')),
                ('project_name', models.ForeignKey(to='tasks.Project')),
                ('requires', models.ForeignKey(blank=True, to='tasks.Task', null=True)),
                ('target', models.ForeignKey(to='tasks.Target')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='arguments',
            name='name',
        ),
        migrations.RemoveField(
            model_name='headers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='arguments',
        ),
        migrations.DeleteModel(
            name='Arguments',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='headers',
        ),
        migrations.DeleteModel(
            name='Headers',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='requires',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='target',
        ),
        migrations.AlterField(
            model_name='history',
            name='task_name',
            field=models.ForeignKey(to='tasks.Task'),
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
