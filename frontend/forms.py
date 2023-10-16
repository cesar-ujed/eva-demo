from django import forms
from api.models import *

class RecomendacionForm(forms.ModelForm):
    class Meta:
        model = Recomendacion
        fields = '__all__'
        exclude = ['observacion']