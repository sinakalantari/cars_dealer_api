from django.contrib.auth.models import User
from django.db import models
from cars_inventory.models import Location
from django_jalali.db import models as jmodel
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    SYSTEM_ADMIN = 1
    MANAGEMENT = 2
    SUPERVISOR = 3
    CLIENT = 4
    ROLE_CHOICES = (
        (SYSTEM_ADMIN, 'ادمین سیستم'),
        (MANAGEMENT, 'مدیریت'),
        (SUPERVISOR, 'سرپرست'),
        (CLIENT, 'کاربر'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class PositionsModel(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = 'سمت'
        verbose_name_plural = 'سمت ها'

    def __str__(self):
        return self.title


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, verbose_name="موقعیت")
    position = models.ForeignKey(PositionsModel, on_delete=models.SET_NULL, null=True, verbose_name="سمت")
    hireDate = jmodel.jDateField(null=True, verbose_name="تاریخ استخدام", blank=True)
    fireDate = jmodel.jDateField(null=True, verbose_name="تاریخ خروج", blank=True)
    buyacc = models.BooleanField(verbose_name="مجوز خرید", default=False)
    sellacc = models.BooleanField(verbose_name="مجوز فروش", default=False)
    deliveracc = models.BooleanField(verbose_name="مجوز تحویل", default=False)
    active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = 'پروفایل کاربر'
        verbose_name_plural = 'پروفایل های کاربر'

    def __str__(self):
        return self.user.__str__()
