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
            'numero_rec': forms.NumberInput(attrs={'class': 'form-control', 'autofocus': 'True'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control'}),
            'meta': forms.Textarea(attrs={'class': 'form-control'}),
            'plazo_cumplimiento': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'indicador_validacion': forms.TextInput(attrs={'class': 'form-control'}),
            'acciones_meta': forms.Textarea(attrs={'class': 'form-control'}),
            'recursos': forms.Textarea(attrs={'class': 'form-control'}),
            'responsables': forms.CheckboxSelectMultiple(),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }


class ArchivoUpForm(forms.ModelForm):
    class Meta:
        model = Archivo 
        fields = ['archivo']   
        widgets = {
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
        }   

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')

        # Validar tipo de archivo
        if not archivo.name.endswith('.pdf'):
            raise forms.ValidationError('Solo se permiten archivos PDF.')

        # Validar tamaño del archivo
        limite = 5 * 1024 * 1024  # 5 MB
        if archivo.size > limite:
            raise forms.ValidationError('El archivo no puede exceder los 5 MB.')

        return archivo