# Generated by Django 3.0.3 on 2020-07-30 10:52

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_inventory', '0007_auto_20200730_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsinventory',
            name='submit_date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='زمان ایجاد'),
        ),
    ]