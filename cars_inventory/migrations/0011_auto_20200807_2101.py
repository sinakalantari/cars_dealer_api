# Generated by Django 3.0.8 on 2020-08-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_inventory', '0010_auto_20200807_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartype',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='location',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
    ]
