#from django.contrib.auth.models import Group
#from allauth.account.models import EmailAddress # VALIDAR EMAIL NO VA (JG)
from django.db.models import Sum
import os
import django
import datetime
import pandas as pd

# project_name nombre del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
django.setup()
from applications.api.models import operaciones, em_sp,ProductionOrders1_SAP, ProductionOrders2_SAP, MaestroDeMateriales
# Lee la base de datos de reportes de batchs 
for x in range(7,12):
    batchs = operaciones.objects.filter(idlote__icontains=x)
    resultado = batchs.aggregate(MPDC00008=Sum('em1'),MPDC00004=Sum('em2')+Sum('em3')+Sum('em4'),MPDC00002=Sum('em5'),AGUA=Sum('em6'),SE_NEUT001=Sum('em7'),MPCL00002=Sum('em8'))
    total = resultado['MPDC00008']+resultado['MPDC00004']+resultado['MPDC00002']+resultado['AGUA']+resultado['SE_NEUT001']+resultado['MPCL00002']
    filas = ProductionOrders2_SAP(
        parentkey = ProductionOrders1_SAP.objects.get(docentry=x),
        linenum = 0,
        itemcode = MaestroDeMateriales.objects.get(id='MPDC00008'),
        plannedqty = resultado['MPDC00008']
    )
    filas.save()
    filas = ProductionOrders2_SAP(
        parentkey =  ProductionOrders1_SAP.objects.get(docentry=x),
        linenum = 1,
        itemcode = MaestroDeMateriales.objects.get(id='MPDC00004'),
        plannedqty = resultado['MPDC00004']
    )
    filas.save()
    filas = ProductionOrders2_SAP(
        parentkey =  ProductionOrders1_SAP.objects.get(docentry=x),
        linenum = 2,
        itemcode = MaestroDeMateriales.objects.get(id='MPDC00002'),
        plannedqty = resultado['MPDC00002']
    )
    filas.save()
    filas = ProductionOrders2_SAP(
        parentkey =  ProductionOrders1_SAP.objects.get(docentry=x),
        linenum = 3,
        itemcode = MaestroDeMateriales.objects.get(id='SE-NEUT001'),
        plannedqty = resultado['SE_NEUT001']
    )
    filas.save()
    filas = ProductionOrders2_SAP(
        parentkey = ProductionOrders1_SAP.objects.get(docentry=x),
        linenum = 4,
        itemcode = MaestroDeMateriales.objects.get(id='MPCL00002'),
        plannedqty = resultado['MPCL00002']
    )
    filas.save()
        
    print(resultado,"  TOTAL:", total)


#ultimoRegistro = int(batchs.hora[0:20].replace(" ", "").replace(":","").replace("-",""))
#print(ultimoRegistro)

### LE LOS REPORTES DE PRODUCCION DE BATCH EN EL PLC
#from pycomm3 import LogixDriver

#with LogixDriver('192.170.4.98') as CLX_Cremas:
    # Escribe las lista de ingredientes de todas las recetas. Tiene MAXIMO 25 registros


#print(plc_batchs.value[20]['hora'])
# j = 0
# ids = []
# reglist = plc_batchs.value
# reglist.reverse()
# for i in reglist:
#     if j>=50:
#         break
#     else:

#         if j>0 and i['hora']!= "" :
#             idbath_num = int(i['hora'][0:20].replace(" ", "").replace(":","").replace("-",""))
#             ids.append(idbath_num)
#             print(ultimoRegistro-idbath_num)
#             if idbath_num>ultimoRegistro:
#                 print("copiar registros")
# #            print(i['hora'], "   ", ids[-1] )
#         j=j+1 #test
# #print(ids)
# #print(max(ids),min(ids))