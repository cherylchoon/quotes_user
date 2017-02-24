# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:16
from __future__ import unicode_literals

import apps.quotes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0007_auto_20170224_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, validators=[apps.quotes.models.lengthGreaterThree])),
                ('message', models.TextField(max_length=1000, validators=[apps.quotes.models.lengthGreaterTen])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quotes', to='login.User')),
            ],
        ),
    ]