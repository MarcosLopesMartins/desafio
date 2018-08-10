# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-10 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invalidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nome'],
                'db_table': 'invalidos',
            },
        ),
    ]
