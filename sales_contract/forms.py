from django import forms
from .models import SaleContract
from django.core import validators
from cars_inventory.models import CarsInventory


class SaleContractForm(forms.ModelForm):
    class Meta:
        model = SaleContract
        fields = ('customerName', 'mobileNumber', 'melliCode', 'address', 'postalCode', 'ChassisNum', 'price')

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        qs = CarsInventory.objects.exclude(chassis_num__in=SaleContract.objects.all().values_list('ChassisNum__chassis_num'))
        self.fields['ChassisNum'].queryset = qs

# class SaleContractForm(forms.ModelForm):
#     customerName = forms.CharField(
#         widget=forms.TextInput(attrs={'style': 'text-transform:uppercase;'}), label='نام مشتری',
#     )
#     mobileNumber = forms.IntegerField(
#         widget=forms.NumberInput, label='شماره تماس',
#     )
#     melliCode = forms.IntegerField(
#         widget=forms.NumberInput, label='کد ملی',
#     )
#     address = forms.CharField(
#         widget=forms.Textarea, label='ادرس',
#     )
#     postalCode = forms.IntegerField(
#         widget=forms.NumberInput, label='کد پستی',
#     )
#     ChassisNum = forms.ModelChoiceField(queryset=CarsInventory.objects.all())
