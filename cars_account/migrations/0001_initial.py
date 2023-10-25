# Generated by Django 3.0.3 on 2020-07-30 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars_inventory', '0008_auto_20200730_1522'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hireDate', django_jalali.db.models.jDateField(verbose_name='تاریخ استخدام')),
                ('fireDate', django_jalali.db.models.jDateField(null=True, verbose_name='تاریخ خروج')),
                ('buyacc', models.BooleanField(verbose_name='مجوز خرید')),
                ('sellacc', models.BooleanField(verbose_name='مجوز فروش')),
                ('deliveracc', models.BooleanField(verbose_name='مجوز تحویل')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars_inventory.Location', verbose_name='موقعیت')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars_account.PositionsModel', verbose_name='سمت')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]