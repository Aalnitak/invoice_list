import xml.etree.ElementTree as et
from zipfile import ZipFile
import os
from .models import Dte , Company , Detalle
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
            rutAux= None
            razonSocialAux= None
            dMonto= None
            dIVA= None
            dTxt= None
            emisor = None
            receptor = None
            comp = Company.objects.all()
            

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

                #first we need to populate Company model
                
                for child in root:                                     
                    # validate if the company already exists 
                    if (child.tag != 'items'):                                                
                        for compa in comp:
                            #when the company doesnt exist
                            if (compa.rut != child.attrib.get("rut") ):
                                rutAux = child.attrib.get("rut")
                                razonSocialAux = child.attrib.get("razonSocial")

                                if (child.tag == 'emisor'):
                                    emisor = Company(rut = rutAux, razonSocial = razonSocialAux)
                                    emisor.save()
                                    break
                                elif (child.tag == 'receptor'):
                                    receptor = Company(rut = rutAux, razonSocial = razonSocialAux)
                                    receptor.save()
                                    break
                            #when it exists
                            else:
                                if (child.tag == 'emisor'):
                                    emisor = compa
                                    break
                                elif (child.tag == 'receptor'):
                                    receptor = compa
                                    break                           
                #we create the DTE object with emisor and receptor ID
                dteAux= Dte(
                    dteEmision = emi,
                    dteTipo = tipo,
                    dteFolio = folio,
                    emisorID = emisor,  
                    receptorID = receptor                  
                )
                #save dte to database
                dteAux.save()
                # we create detalle objects with this DTE ID
                for child in root:
                    if (child.tag == 'items'):                        
                        for item in child:                                                
                            dMonto = item.attrib.get("monto")
                            dIVA = item.attrib.get("iva")
                            dTxt = item.text
                            detalleAux = Detalle(dte = dteAux, monto = dMonto, iva = dIVA, txt = dTxt)
                            detalleAux.save()                   
                             
                #remove unzziped XML file
                os.remove(name)
            

            



        
        