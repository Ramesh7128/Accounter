# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountingapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_company',
            new_name='clientCompany',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_email',
            new_name='clientEmail',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_name',
            new_name='clientName',
        ),
    ]
