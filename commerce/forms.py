from .models import RegistersUser
from django import forms
from django.forms import ModelForm

class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegistersUser
        fields = '__all__'
        labels = {
            "name": "Username",
            "emailId": "Email Id",
            "phoneNum": "Phone number",
            "password": "Password",
        }