from django.db import models
from django_jalali.db import models as jmodels


class CustomerModel(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="نام")
    last_name = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    mobile_num = models.CharField(max_length=11, verbose_name="شماره موبایل")
    address = models.TextField(verbose_name='آدرس')
    melli_code = models.CharField(max_length=10, verbose_name='کد ملی')
    postal_code = models.CharField(max_length=10, verbose_name='کد پستی')
    creation_date = jmodels.jDateField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



