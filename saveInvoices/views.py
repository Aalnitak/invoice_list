from django.shortcuts import render, redirect
from django.utils import timezone
from .models import dte
from .tree import cargarDatos



def invoice_list (request):
    #clean the database
    dte.objects.all().delete()
    #import the data from the dte-files.zip
    cargarDatos()
    #order by emission date descending
    #if dates mach order by folio
    invoices = dte.objects.all().order_by("-dteEmision" , "dteFolio")
    #render the view
    return render(request, 'saveInvoices/invoices_list.html', {'invoices':invoices})