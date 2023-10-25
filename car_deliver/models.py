from django.db import models
from django_jalali.db import models as jmodels
from sales_contract.models import SaleContract
from cars_account.models import UserProfileModel


class CarDeliverModel(models.Model):
    contract = models.ForeignKey(SaleContract, on_delete=models.CASCADE)
    deliver_expert = models.ForeignKey(UserProfileModel, on_delete=models.SET_NULL, null=True)
    deliver_date = jmodels.jDateField
    receiver = models.CharField(max_length=150)
    deliver_status = models.CharField(max_length=150, choices={(1, 'سالم'), (2, 'ناسالم')})
    damage_description = models.TextField

    class Meta:
        verbose_name = 'تحویل خودرو'
        verbose_name_plural = 'تحویل خودروها'

    def __str__(self):
        return self.contract.__str__()
