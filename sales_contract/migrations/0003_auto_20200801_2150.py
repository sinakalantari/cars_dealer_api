# Generated by Django 3.0.3 on 2020-08-01 17:20

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_contract', '0002_salemethodmodel_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salemethodmodel',
            name='time',
        ),
        migrations.AlterField(
            model_name='salecontract',
            name='creationtime',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
    ]