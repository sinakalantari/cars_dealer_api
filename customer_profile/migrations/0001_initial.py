# Generated by Django 3.0.3 on 2020-07-31 11:13

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='نام')),
                ('last_name', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('mobile_num', models.CharField(max_length=11, verbose_name='شماره موبایل')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('melli_code', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('postal_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('creation_date', django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتریان',
            },
        ),
    ]
