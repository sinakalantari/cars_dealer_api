from django.db import models
from cars_inventory.models import CarsInventory
from customer_profile.models import CustomerModel
from django_jalali.db import models as jmodels
from cars_account.models import UserProfileModel


class LeasingNameModel(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = 'لیزینگ'
        verbose_name_plural = 'لیزینگ ها'

    def __str__(self):
        return self.title


class SaleMethodModel(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = 'طرح فروش'
        verbose_name_plural = 'طرح های فروش'

    def __str__(self):
        return self.title


class SaleContract(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, null=True, verbose_name='مشتری')
    chassisnum = models.ForeignKey(CarsInventory, on_delete=models.CASCADE, null=False, blank=False,
                                   verbose_name='شماره شاسی')
    creationtime = jmodels.jDateField(auto_now_add=True)
    sale_price = models.IntegerField(verbose_name='قیمت فروش')
    contractdate = jmodels.jDateField(verbose_name="تاریخ قرارداد")
    sell_type = models.CharField(max_length=10, choices=[(1, "نقد"), (2, "اقساط")], verbose_name="نوع فروش")
    leasing_name = models.ForeignKey(LeasingNameModel, on_delete=models.SET_NULL, null=True, verbose_name="نام لیزینگ")
    period = models.IntegerField(verbose_name="مدت بازپرداخت")
    loan_amount = models.IntegerField(verbose_name="مبلغ تسهیلات")
    sale_expert = models.ForeignKey(UserProfileModel, on_delete=models.SET_NULL, null=True, verbose_name="کارشناس فروش")
    sale_method = models.ForeignKey(SaleMethodModel, on_delete=models.SET_NULL, null=True, verbose_name="طرح فروش")
    description = models.TextField(verbose_name='توضیحات')
    payment = models.BooleanField(default=False, verbose_name='تکمیل پرداخت')

    class Meta:
        verbose_name = 'قرارداد'
        verbose_name_plural = 'قرارداد ها'

    def __str__(self):
        return f"{self.customer.__str__()} {self.chassisnum.name}"
