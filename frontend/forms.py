from django import forms
from api.models import *
from django.contrib.auth.forms import AuthenticationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'contraseña'}))

class RecomendacionForm(forms.ModelForm):
    class Meta:
        model = Recomendacion
        fields = '__all__'
        exclude = ['observacion']