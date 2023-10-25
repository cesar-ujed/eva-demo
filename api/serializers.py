from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'


class Eje_evalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eje_eval
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'


class RecomendacionSerializer(serializers.ModelSerializer):

    categoria = serializers.CharField(
        source='categoria.eje', trim_whitespace=True, required=False, allow_blank=True, allow_null=True)
    
    class Meta:
        model = Recomendacion
        fields = '__all__'
