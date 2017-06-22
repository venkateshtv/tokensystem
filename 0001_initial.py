# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-15 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCountOfToken',
            fields=[
                ('num_count', models.IntegerField(default=0)),
                ('vendor_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('token_date', models.DateField(primary_key=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.IntegerField(default=0)),
                ('barcodeName', models.CharField(max_length=500)),
                ('barcode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenDateTime', models.DateTimeField()),
                ('barcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Barcode')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Vendor'),
        ),
    ]
