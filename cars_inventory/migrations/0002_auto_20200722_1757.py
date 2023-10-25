# Generated by Django 3.0.8 on 2020-07-22 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarsColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
            ],
        ),
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'مدل',
                'verbose_name_plural': 'مدل ها',
            },
        ),
        migrations.AlterModelOptions(
            name='carsbrand',
            options={'verbose_name': 'برند', 'verbose_name_plural': 'برند ها'},
        ),
        migrations.AddField(
            model_name='carsinventory',
            name='chassis_num',
            field=models.CharField(default=0, max_length=150, verbose_name='شماره شاسی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carsinventory',
            name='year_model',
            field=models.IntegerField(default=0, verbose_name='سال ساخت'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carsinventory',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars_inventory.CarsBrand', verbose_name='برند'),
        ),
        migrations.CreateModel(
            name='CarsName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_inventory.CarsModel', verbose_name='مدل')),
            ],
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_inventory.CarsBrand', verbose_name='برند'),
        ),
        migrations.AddField(
            model_name='carsinventory',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars_inventory.CarsColor', verbose_name='رنگ'),
        ),
        migrations.AddField(
            model_name='carsinventory',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars_inventory.CarsModel', verbose_name='مدل'),
        ),
        migrations.AddField(
            model_name='carsinventory',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars_inventory.CarsName', verbose_name='نام خودرو'),
        ),
    ]
