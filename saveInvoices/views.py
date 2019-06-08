from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Dte, Company, Detalle
from .tree import cargarDatos



def invoice_list (request):
    #clean the database
    Detalle.objects.all().delete()
    Dte.objects.all().delete()
    Company.objects.all().delete()    
    #import the data from the dte-files.zip
    cargarDatos()
    #order by emission date descending
    #if dates match order by folio
    dtes = Dte.objects.all().order_by("-dteEmision" , "dteFolio")
    compa = Company.objects.all()
    deta = Detalle.objects.all()
    #render the view
    return render(request, 'saveInvoices/invoices_list.html',{'dtes':dtes ,'compa':compa , 'deta':deta} )