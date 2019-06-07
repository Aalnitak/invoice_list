import xml.etree.ElementTree as et
from zipfile import ZipFile
import os
from .models import dte
from datetime import datetime 

def cargarDatos():
    
    
    fileName = "saveInvoices/dte-files.zip"

    with ZipFile(fileName, 'r') as zip:
        #capture name list
        names = zip.namelist() 
        for name in names:
            #initialize variables to null
            emi= None
            tipo= None
            folio= None
            emirut= None
            emiRS= None
            recrut= None
            recRS= None
            d1monto= None
            d1IVA= None
            d1txt= None
            d3monto = None
            d3IVA = None
            d3txt = None
            d2monto = None
            d2IVA = None
            d2txt = None

            #skip MACOSX filenames
            if 'MACOSX' not in name:
                zip.extract(name)
                tree = et.parse(name)
                root = tree.getroot()
                #transform UNIX to DateTime and capture the required information
                emiAUX = int(root.attrib.get("emision"))
                emi = datetime.utcfromtimestamp(emiAUX).strftime('%Y-%m-%d %H:%M:%S')
                tipo = root.attrib.get("tipo")
                folio = root.attrib.get("folio")  
                
                for child in root:                   
                    if (child.tag == 'emisor'):
                        emirut = child.attrib.get("rut")
                        emiRS = child.attrib.get("razonSocial")
                    elif (child.tag == 'receptor'):
                        recrut = child.attrib.get("rut")
                        recRS = child.attrib.get("razonSocial")                  
                    
                    if (child.tag == 'items'):
                        i=0
                        for item in child:                                                
                            if (i==0):
                                d1monto = item.attrib.get("monto")
                                d1IVA = item.attrib.get("iva")
                                d1txt = item.text
                            elif(i==1):
                                d2monto = item.attrib.get("monto")
                                d2IVA = item.attrib.get("iva")
                                d2txt = item.text
                            elif(i==2):
                                d3monto = item.attrib.get("monto")
                                d3IVA = item.attrib.get("iva")
                                d3txt = item.text
                            i=i+1
                        
                #create the tuple with each XML file
                dteAux= dte(
                    dteEmision = emi,
                    dteTipo = tipo,
                    dteFolio = folio,
                    emisorRut = emirut,
                    emisorRazonSocial = emiRS,
                    receptorRut = recrut,
                    receptorRazonSocial = recRS,
                    detalle1Monto = d1monto,
                    detalle1Iva = d1IVA,
                    detalle1Txt = d1txt,
                    detalle2Monto = d2monto,
                    detalle2Iva = d2IVA,
                    detalle2Txt = d2txt,
                    detalle3Monto = d3monto,
                    detalle3Iva = d3IVA,
                    detalle3Txt = d3txt
                )
                #save it to the badaBase
                dteAux.save()                
                #remove unzziped XML file
                os.remove(name)
            

            



        
        