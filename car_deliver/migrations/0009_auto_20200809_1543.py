# Generated by Django 3.0.8 on 2020-08-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_deliver', '0008_auto_20200808_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardelivermodel',
            name='deliver_status',
            field=models.CharField(choices=[(2, 'ناسالم'), (1, 'سالم')], max_length=150),
        ),
    ]