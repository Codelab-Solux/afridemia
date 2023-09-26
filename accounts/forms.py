from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"
        self.fields['password2'].widget.attrs['class'] = "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"
        self.fields['password1'].label = "Mot de pass"
        self.fields['password2'].label = "Confirmez votre mot de pass"

    class Meta:
        model = CustomUser
        fields = (
            'email', 'first_name',
            'last_name',
            'password1',
            'password2',
        )
        labels = {
            'email': 'Email',
            'first_name': 'Prenoms',
            'last_name': 'Nom',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')
        exclude = ('groups', 'user_permissions',
                   'password', 'last_login', 'is_staff', 'is_superuser', 'is_active')
        labels = {'phone': 'Téléphone', }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
        }


class AdminEditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('__all__')
        exclude = ('groups', 'user_permissions',
                   'password', 'last_login', 'is_staff', 'is_superuser')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'last_name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'email': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'username': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'phone': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md ring-transparent ring-2 focus:ring-green-300 text-black w-full outline-none"}),
            'is_staff': forms.BooleanField(),
            'is_superuser': forms.BooleanField(),
        }
