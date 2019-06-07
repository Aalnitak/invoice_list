from django.db import models

# Create your models here.

#dte model to capture all data from XML
class dte(models.Model):
    dteEmision = models.DateTimeField()
    dteTipo = models.CharField(max_length=50)
    dteFolio = models.IntegerField()

    emisorRut = models.CharField(max_length=50)
    emisorRazonSocial = models.CharField(max_length=50)

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