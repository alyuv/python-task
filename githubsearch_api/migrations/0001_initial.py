# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('html_url', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('stargazers_count', models.DecimalField(decimal_places=0, max_digits=5)),
                ('lang', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'repository',
            },
        ),
    ]
