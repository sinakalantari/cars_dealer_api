# Generated by Django 3.0.3 on 2020-07-31 20:46

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales_contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'نوع پرداخت',
                'verbose_name_plural': 'انواع پرداخت',
            },
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='مبلغ پرداختی')),
                ('payment_date', django_jalali.db.models.jDateField(verbose_name='تاریخ پرداخت')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_contract.SaleContract', verbose_name='قرارداد')),
                ('payment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.PaymentTypeModel', verbose_name='نوع پرداخت')),
            ],
            options={
                'verbose_name': 'پرداخت',
                'verbose_name_plural': 'پرداخت ها',
            },
        ),
    ]
