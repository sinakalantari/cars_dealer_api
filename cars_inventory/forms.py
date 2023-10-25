from django import forms
from .models import CarsInventory, CarsBrand, CarsModel, CarsColor, CarsName


class InventoryCars(forms.Form):
    brand = CarsBrand.objects.all()

    cars_brand = forms.CharField(max_length=150, widget=forms.Select(choices=brand))


class TestInventory(forms.ModelForm):
    class Meta:
        model = CarsInventory
        fields = ('brand', 'model', 'name', 'color', 'year_model', 'chassis_num')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = CarsModel.objects.none()
        self.fields['name'].queryset = CarsName.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = CarsModel.objects.filter(brand_id=brand_id).order_by('title')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.brand.model_set.order_by('title')

        if 'model' in self.data:
            try:
                model_id = int(self.data.get('model'))
                self.fields['name'].queryset = CarsName.objects.filter(model_id=model_id).order_by('title')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['name'].queryset = self.instance.model.name_set.order_by('title')
