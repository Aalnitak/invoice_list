from django.db import models

# Create your models here.

#dte model to capture all data from XML
class dte(models.Model):
    dteEmision = models.DateTimeField()
    dteTipo = models.CharField(max_length=50)
    dteFolio = models.IntegerField()

    #emisorID = pk_company
    emisorRut = models.CharField(max_length=50)
    emisorRazonSocial = models.CharField(max_length=50)
    #receptorID = pk_company
    receptorRut = models.CharField(max_length=50)
    receptorRazonSocial = models.CharField(max_length=50)

    detalle1Monto = models.IntegerField()
    detalle1Iva = models.IntegerField()
    detalle1Txt = models.CharField(max_length=50)

    detalle2Monto = models.IntegerField(null=True, blank = True)
    detalle2Iva = models.IntegerField(null=True, blank = True)
    detalle2Txt = models.CharField(max_length=50,null=True, blank = True)

    detalle3Monto = models.IntegerField(null=True, blank = True)
    detalle3Iva = models.IntegerField(null=True, blank = True)
    detalle3Txt = models.CharField(max_length=50,null=True, blank = True)

    def __str__(self):
        return self.dteEmision + " " + self.dteTipo + " " + self.dteFolio

#quizas falta fk de pk_dte
class detalle(models.Model):
    monto = models.IntegerField()
    iva = models.IntegerField()
    txt = models.CharField(max_length=100)

    def __str__(self):
        return txt

class company(models.Model):
    rut = models.CharField(maxlength=50)
    razonSocial = models.CharField(max_length=50)

    def __str__(self):
        return razonSocial 