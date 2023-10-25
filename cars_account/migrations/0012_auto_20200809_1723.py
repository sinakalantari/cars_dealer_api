# Generated by Django 3.0.8 on 2020-08-09 12:53

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_account', '0011_auto_20200809_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='buyacc',
            field=models.BooleanField(default=False, verbose_name='مجوز خرید'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='hireDate',
            field=django_jalali.db.models.jDateField(default=None, null=True, verbose_name='تاریخ استخدام'),
        ),
    ]