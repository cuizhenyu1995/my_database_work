# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buy_device',
            fields=[
                ('buy_no', models.AutoField(serialize=False, primary_key=True)),
                ('de_no', models.CharField(max_length=50)),
                ('de_btime', models.DateTimeField()),
                ('de_ptime', models.DateTimeField()),
                ('buy_num', models.IntegerField()),
                ('beizhu', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('de_no', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('de_name', models.CharField(max_length=50)),
                ('de_allnum', models.IntegerField()),
                ('de_repnum', models.IntegerField()),
                ('de_lennum', models.IntegerField()),
                ('de_lasnum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lend_device',
            fields=[
                ('lend_no', models.AutoField(serialize=False, primary_key=True)),
                ('de_no', models.CharField(max_length=50)),
                ('st_no', models.CharField(max_length=50)),
                ('lend_date', models.DateTimeField()),
                ('lend_num', models.IntegerField()),
                ('beizhu', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='repair_device',
            fields=[
                ('repair_no', models.AutoField(serialize=False, primary_key=True)),
                ('st_no', models.CharField(max_length=50)),
                ('de_no', models.CharField(max_length=50)),
                ('destroy_date', models.DateTimeField()),
                ('repair_num', models.IntegerField()),
                ('beizhu', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('st_username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('st_name', models.CharField(max_length=50)),
                ('st_sex', models.IntegerField(choices=[(1, b'Male'), (2, b'Female')])),
                ('st_age', models.CharField(max_length=50)),
                ('st_password', models.CharField(max_length=50)),
                ('st_address', models.CharField(max_length=250)),
            ],
        ),
    ]
