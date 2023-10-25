from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری را وارد نمایید'}),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور را وارد نمایید'}),
        label='کلمه عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exist_user = User.objects.filter(username=user_name).exists()
        if not is_exist_user:
            raise forms.ValidationError('نام کاربری وجود ندارد')
        return user_name