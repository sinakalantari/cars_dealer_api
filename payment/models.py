from django.db import models
from django_jalali.db import models as jmodels
from sales_contract.models import SaleContract

import os


def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name = f"{instance.contract.id}{ext}"
    return f"payment/{instance.payment_date}/{final_name}"


class PaymentTypeModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        verbose_name = 'نوع پرداخت'
        verbose_name_plural = 'انواع پرداخت'

    def __str__(self):
        return self.title


class PaymentModel(models.Model):
    payment_type = models.ForeignKey(PaymentTypeModel, on_delete=models.SET_NULL, null=True, verbose_name='نوع پرداخت')
    contract = models.ForeignKey(SaleContract, on_delete=models.CASCADE, verbose_name='قرارداد')
    amount = models.IntegerField(verbose_name='مبلغ پرداختی')
    payment_date = jmodels.jDateField(verbose_name='تاریخ پرداخت')
    payment_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت ها'

    def __str__(self):
        return self.contract.__str__()
