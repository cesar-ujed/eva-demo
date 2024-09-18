from django import forms
from api.models import *
from django.contrib.auth.forms import AuthenticationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'contraseña'}))

class RecomendacionForm(forms.ModelForm):
    observacion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False  # El campo no será obligatorio en el formulario
    )

    class Meta:
        model = Recomendacion
        fields = '__all__'
        widgets = {
            'numero_rec': forms.NumberInput(attrs={'class': 'form-control'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control'}),
            'meta': forms.Textarea(attrs={'class': 'form-control'}),
            'plazo_cumplimiento': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'indicador_validacion': forms.TextInput(attrs={'class': 'form-control'}),
            'acciones_meta': forms.Textarea(attrs={'class': 'form-control'}),
            'recursos': forms.Textarea(attrs={'class': 'form-control'}),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            # Puedes eliminar la entrada de 'observacion' aquí si defines el campo arriba
        }
