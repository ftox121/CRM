from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from crm.models import Profile, CRUDModel, ClientModel

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class RegisterForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = CRUDModel
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = '__all__'