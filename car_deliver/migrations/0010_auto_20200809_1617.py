# Generated by Django 3.0.8 on 2020-08-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_deliver', '0009_auto_20200809_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardelivermodel',
            name='deliver_status',
            field=models.CharField(choices=[(1, 'سالم'), (2, 'ناسالم')], max_length=150),
        ),
    ]