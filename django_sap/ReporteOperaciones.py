#from django.contrib.auth.models import Group
#from allauth.account.models import EmailAddress # VALIDAR EMAIL NO VA (JG)
#from django.db import models
import os
import django
import datetime
import pandas as pd

# project_name nombre del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
django.setup()
from applications.api.models import operaciones
# Lee la base de datos de reportes de batchs 
batchs = operaciones.objects.last()
ultimoRegistro = int(batchs.hora[0:20].replace(" ", "").replace(":","").replace("-",""))
#print(ultimoRegistro)



### LE LOS REPORTES DE PRODUCCION DE BATCH EN EL PLC
from pycomm3 import LogixDriver

with LogixDriver('192.170.4.98') as CLX_Cremas:
    # Escribe las lista de ingredientes de todas las recetas. Tiene MAXIMO 25 registros

    plc_batchs = CLX_Cremas.read('registros_batch{50}') # lee el TAG UDT en un arreglo de 50 registros iniciando del 0 al 49


#print(len(plc_batchs[0]))

#print(plc_batchs.value[20]['hora'])
j = 0
ids = []
reglist = plc_batchs.value
reglist.reverse()
for i in reglist:
    if j>=50:
        break
    else:
        
        if j<49 and i['hora']!= "" :
            idbath_num = int(i['hora'][0:20].replace(" ", "").replace(":","").replace("-",""))
            print(ultimoRegistro-idbath_num)
            if idbath_num>ultimoRegistro:
                print("copiar registros")
                operacion = operaciones(
                        hora      = i['hora'],
                        hora_fin  = i['hora_fin'],
                        em1_time  = i['em1_time'],
                        em1       = i['em1'],
                        em2_time  = i['em2_time'],
                        em2       = i['em2'],
                        em3_time  = i['em3_time'],
                        em3       = i['em3'],
                        em4_time  = i['em4_time'],
                        em4       = i['em4'],
                        em5_time  = i['em5_time'],
                        em5       = i['em5'],
                        em6_time  = i['em6_time'],
                        em6       = i['em6'],
                        em7_time  = i['em7_time'],
                        em7       = i['em7'],
                        em8_time  = i['em8_time'],
                        em8       = i['em8'],
                        em9_time  = i['em9_time'],
                        em9       = i['em9'],
                        em10_time  = i['em10_time'],
                        em10       = i['em10'],
                        em11_time  = i['em11_time'],
                        em11       = i['em11'],
                        em12_time  = i['em12_time'],
                        em12       = i['em12'],
                        em13_time  = i['em13_time'],
                        em13       = i['em13'],
                        em14_time  = i['em14_time'],
                        em14       = i['em14'],
                        em15_time  = i['em15_time'],
                        em15       = i['em15'],
                        em16_time  = i['em16_time'],
                        em16       = i['em16'],
                        em17_time  = i['em17_time'],
                        em17       = i['em17'],
                        em20_time  = i['em20_time'],
                        em20       = i['em20'],                        
                        em21_time  = i['em21_time'],
                        em21       = i['em21'],
                        idlote     = i['id_lote'],
                        receta_id  = i["id_receta"],
                        receta_total_set_kg = i['setpoint']
                        
                        )
                operacion.save()
        j=j+1 #test
