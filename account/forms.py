from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام کاربری'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'رمز عبور'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'تکرار رمز عبور'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ایمیل'})

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]




class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        