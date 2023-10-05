from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets


# ViewSets define the view behavior.
class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class Eje_evalViewSet(viewsets.ModelViewSet):
    queryset = Eje_eval.objects.all()
    serializer_class = Eje_evalSerializer    


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ResponsableViewSet(viewsets.ModelViewSet):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer


class RecomendacionViewSet(viewsets.ModelViewSet):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer
    


