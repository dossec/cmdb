# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-07 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0017_asset_wan_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisqueCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='disque cluster alias name')),
                ('addr', models.CharField(blank=True, default=b'', max_length=128, null=True, verbose_name='disque address')),
            ],
        ),
    ]
