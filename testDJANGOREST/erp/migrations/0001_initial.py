# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('ean13', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_item', to='erp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.Supplier'),
        ),
    ]
