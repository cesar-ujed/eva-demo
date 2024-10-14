from django.db import models

# Create your models here.
class Evaluacion(models.Model):
    nombre      = models.CharField(max_length=90)
    fecha_eva   = models.DateField(auto_now_add=False, null=True)
    fecha_pmyac = models.DateField(auto_now_add=False, null=True)

    def __str__(self):
        return self.nombre
    

class Eje_eval(models.Model):
    numero_eje = models.IntegerField()
    nombre_eje = models.CharField(max_length=90)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_eje
    

class Categoria(models.Model):
    numero_cat  = models.IntegerField()
    nombre_cat  = models.CharField(max_length=90)
    eje         = models.ForeignKey(Eje_eval, on_delete=models.CASCADE)   

    def __str__(self):
        return self.nombre_cat
    
    
class Responsable(models.Model):
    area_resp = models.CharField(max_length=60)

    def __str__(self):
        return self.area_resp


class Recomendacion(models.Model):
    numero_rec              = models.IntegerField()
    recomendacion           = models.TextField()
    meta                    = models.TextField()
    plazo_cumplimiento      = models.DateField(auto_now_add=False, null=True)
    indicador_validacion    = models.CharField(max_length=255)
    acciones_meta           = models.TextField()
    recursos                = models.TextField()
    responsables            = models.ManyToManyField(Responsable)
    categoria               = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacion             = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.recomendacion, self.categoria


class Archivo(models.Model):
    archivo         = models.FileField(null=True)
    recomendacion   = models.ForeignKey(Recomendacion, related_name='archivos', on_delete=models.CASCADE)