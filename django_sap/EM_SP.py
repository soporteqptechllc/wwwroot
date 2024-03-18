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
from applications.api.models import operaciones, em_sp
# Lee la base de datos de reportes de batchs 

### LE LOS REPORTES DE PRODUCCION DE BATCH EN EL PLC
from pycomm3 import LogixDriver

with LogixDriver('192.170.4.98') as CLX_Cremas:
    # Escribe las lista de ingredientes de todas las recetas. Tiene MAXIMO 25 registros

    EM_SP = CLX_Cremas.read('EM_SP{22}')
for i in EM_SP.value:
    print(i)
    print(i['EM'])
    em_setpoint = em_sp(
        em = int(i['EM']),
        ID = i['ID'],
        Ingrediente = i['Ingrediente'],
        SP = float(i['SP'])
    )
    em_setpoint.save()