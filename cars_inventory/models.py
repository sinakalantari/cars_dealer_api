from django.db import models
from django_jalali.db import models as jmodels


class StatusModel(models.Model):
    title = models.CharField(max_length=150, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت ها'

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = 'موقعیت'
        verbose_name_plural = 'موقعیت ها'

    def __str__(self):
        return self.title


class CarType(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = 'نوع خودرو'
        verbose_name_plural = 'انواع خودرو'

    def __str__(self):
        return self.title


class CarsBrand(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class CarsModel(models.Model):
    brand = models.ForeignKey(CarsBrand, on_delete=models.CASCADE, verbose_name='برند')
    title = models.CharField(max_length=150, verbose_name='عنوان')

    class Meta:
        verbose_name = 'مدل'
        verbose_name_plural = 'مدل ها'

    def __str__(self):
        return self.title


class CarsName(models.Model):
    model = models.ForeignKey(CarsModel, on_delete=models.CASCADE, verbose_name='مدل')
    title = models.CharField(max_length=150, verbose_name='عنوان')

    class Meta:
        verbose_name = 'نام خودرو'
        verbose_name_plural = 'نام خودرو'

    def __str__(self):
        return self.title


class CarsColor(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    def __str__(self):
        return self.title


class CarsInventory(models.Model):
    brand = models.ForeignKey(CarsBrand, on_delete=models.SET_NULL, null=True, verbose_name='برند')
    model = models.ForeignKey(CarsModel, on_delete=models.SET_NULL, null=True, verbose_name='مدل')
    name = models.ForeignKey(CarsName, on_delete=models.SET_NULL, null=True, verbose_name='نام خودرو')
    color = models.ForeignKey(CarsColor, on_delete=models.SET_NULL, null=True, verbose_name='رنگ')
    year_model = models.IntegerField(verbose_name='سال ساخت')
    chassis_num = models.CharField(max_length=150, null=False, blank=False, verbose_name='شماره شاسی')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, verbose_name="موقعیت")
    submit_date = jmodels.jDateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True, verbose_name="نوع خودرو")
    owner = models.CharField(max_length=150, null=True, verbose_name="مالک خودرو")
    price = models.IntegerField(null=True, verbose_name="قیمت")
    purchase_date = jmodels.jDateField(null=True, verbose_name="تاریخ ایجاد")
    status = models.ForeignKey(StatusModel, on_delete=models.SET_NULL, null=True, default=1, verbose_name='وضعیت')

    objects = jmodels.jManager()

    class Meta:
        verbose_name = 'موجودی خودرو'
        verbose_name_plural = 'موجودی خودرو ها'

    def __str__(self):
        return self.chassis_num
