from django.db import models

# Create your models here.

class Company(models.Model):
    rut = models.CharField(max_length=50)
    razonSocial = models.CharField(max_length=50)

    def __str__(self):
        return razonSocial 

#dte model to capture all data from XML
class Dte(models.Model):
    dteEmision = models.DateTimeField()
    dteTipo = models.CharField(max_length=50)
    dteFolio = models.IntegerField()

    #emisorID = pk_company
    emisorID = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='emisor', null = True, blank = True)
    #receptorID = pk_company
    receptorID = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='receptor', null = True, blank = True)

    def __str__(self):
        return "%s %s %s" % (self.dteEmision , self.dteTipo , self.dteFolio)

#quizas falta fk de pk_dte
class Detalle(models.Model):
    dte = models.ForeignKey(Dte, on_delete=models.CASCADE,null = True, blank = True)
    monto = models.IntegerField()
    iva = models.IntegerField()
    txt = models.CharField(max_length=100)

    def __str__(self):
        return txt