# Generated by Django 3.0.8 on 2020-07-23 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_inventory', '0002_auto_20200722_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carscolor',
            options={'verbose_name': 'رنگ', 'verbose_name_plural': 'رنگ ها'},
        ),
        migrations.AlterModelOptions(
            name='carsinventory',
            options={'verbose_name': 'موجودی خودرو', 'verbose_name_plural': 'موجودی خودرو ها'},
        ),
        migrations.AlterModelOptions(
            name='carsname',
            options={'verbose_name': 'نام خودرو', 'verbose_name_plural': 'نام خودرو'},
        ),
    ]
