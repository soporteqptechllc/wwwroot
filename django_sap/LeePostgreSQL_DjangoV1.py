#from django.contrib.auth.models import Group
#from allauth.account.models import EmailAddress # VALIDAR EMAIL NO VA (JG)
#from django.db import models
import os
import django
import datetime
import pandas as pd
# Recetas que actualmente se hacen en CREMAS
recipe_of_cremas = [
    'SE-CRALEGPAIS001',
    'SE-CRANTIBAC002',
    'SE-CRCLASIC003',
    'SE-CRCOCO001',
    'SE-CRECOGREEN001',
    'SE-CRLAVANDA001',
    'SE-CRNARANJA003',
    'SE-CRPERLA001',
    'SE-CRROSA001',
    'SE-CRROSA002',
    'SE-CRROSA003',
    'SE-CRVERDE001',
    'SE-CRVERDE002',
    'SE-CRVERDE003']


# project_name nombre del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
django.setup()
from applications.api.models import RecipesSAP, Recetas, MaestroDeMateriales, ReporteBatch, ReporteSAP, RecetasSAP, Ingredientes
# Lee la base de datos de RecetasSAP
datosRecetasSap = RecetasSAP.objects.all()
# Genera la lista de ingredientes totales basados en las recetas encontradas.
txtSemi = ''
ListIngredient = []
for k in recipe_of_cremas:
    for i in datosRecetasSap:
        txtSemi = str(i.id_semielaborado)
        if k == txtSemi:
            txtIngre = str(i.id_ingrediente)
            if txtIngre in ListIngredient:
                pass
            else:
                ListIngredient.append(txtIngre)
ListaOrdenada = sorted(ListIngredient)     
# Busar los valores de los ingredientes por receta y grabarlos en el mismo orden.
# La Matriz de valores es 30 altos por 25 de ancho. Alto son la cantidad de recetas en listaDeSemi[0] (max 30) y lo ancho son la cantida de valores en listaDeSemi[0].kilogramos[0] (max 25)
# MzValores[] -> [listaDeSemi[0].id maximo de 30 id de recetas,listaDeSemi[0].kilogramos[0] maxmio 25 valores]
# Definiendo el número de filas y columnas
filas = 40
columnas = 40

# Creando una lista vacía
MzValores = []

# Creando un bucle para agregar las filas
for i in range(filas):
    # Creando una fila vacía
    fila = []
    
    # Creando un bucle para agregar las columnas
    for j in range(columnas):
        # Pidiendo al usuario el valor de la celda
        celda = 0.0
        # Agregando la celda a la fila
        fila.append(celda)
    
    # Agregando la fila a la lista de dos dimensiones
    MzValores.append(fila)


listSumaReceta = []
f = 0 
exx = 0
for k in recipe_of_cremas: # recorres todas las recetas
    c = 0
    sumaTotReceta = 0
    for ingrediente in ListaOrdenada:    # recorre todos los nombres de ingredientes 
        for i in datosRecetasSap:
            txtSemi = str(i.id_semielaborado)
            txtIngrediente = str(i.id_ingrediente)
            if (k == txtSemi and ingrediente == txtIngrediente):
                #print(f,c,exx,i.valor, float(i.valor))
                exx=exx+1
                MzValores[f][c]=float(i.valor)
                sumaTotReceta  = sumaTotReceta + float(i.valor)
        c=c+1
    f=f+1
    listSumaReceta.append(sumaTotReceta)


MdeMateriales = MaestroDeMateriales.objects.all()
#print(MdeMateriales)
hoy = datetime.datetime.today()
# crea una lista con las descripciones de los ingredietes a partir de la lista de id ordenada de ingrediente
txtMdeM = ''
ListaOrdenadaName = []
for k in ListaOrdenada:
    for i in MdeMateriales:
        txtMdeM = str(i.id)
        if k == txtMdeM:
            ListaOrdenadaName.append(str(i.name))
# crea una lista con las descripciones de las recetas de semielaborados a partir de la lista de recetas posibles de CREMAS
txtMdeM = ''
ListSEMIName = []
for k in recipe_of_cremas:
    encontrada = False # bandaera para saber si encontre el ID y su descripcion de la receta en el maestro de materiales
    for i in MdeMateriales:
        txtMdeM = str(i.id)
        if k == txtMdeM:
            ListSEMIName.append(str(i.name))
            encontrada = True
    if not encontrada:
        ListSEMIName.append('SIN DESCRIPCION EN MAESTRO DE MATERIALES')

#print(ListSEMIName, len(ListSEMIName))
### ESCRITURA AL PLC
from pycomm3 import LogixDriver

with LogixDriver('192.170.4.98') as CLX_Cremas:
    # Escribe las lista de ingredientes de todas las recetas. Tiene MAXIMO 25 registros
    k=0
    for ing in ListaOrdenada:
            CLX_Cremas.write(f'listaIngredientes[{k}].id_ingrediente',ing)
            CLX_Cremas.write(f'listaIngredientes[{k}].nombre',ListaOrdenadaName[k])
            k+=1
    if k <= 24:
        for j in range(k,25):
            CLX_Cremas.write(f'listaIngredientes[{j}].id_ingrediente','')
            CLX_Cremas.write(f'listaIngredientes[{j}].nombre','')

    
    #Escribe las lista de Nombre de las Recetas de Semielaborados o SEMI tiene MAXIMO 30 registros
    k=0
    for recipe in recipe_of_cremas:
            CLX_Cremas.write(f'listaDeSemi[{k}].id',recipe)
            CLX_Cremas.write(f'listaDeSemi[{k}].nombre',ListSEMIName[k])
            k+=1
    if k <= 29:
        for j in range(k,30):
            CLX_Cremas.write(f'listaDeSemi[{j}].id','')
            CLX_Cremas.write(f'listaDeSemi[{j}].nombre','')



    #PRUEBA
    rows =[]
    id_recetaSelected = CLX_Cremas.read('RecetaSelected.id')
    name_recetaSelected = CLX_Cremas.read('RecetaSelected.nombre')
 #   print(id_recetaSelected.value,"  ",name_recetaSelected.value,"--\n")
    for i in range(20):
        filas=CLX_Cremas.read(f'RecetaSelected.kilogramos[{i}]')
        rows.append(filas.value)
#    print(rows)

    #

    ### escritura de kilogramos por receta.
    # 
    # La Matriz de valores es 30 altos por 25 de ancho. 
    #  -. Alto son la cantidad de recetas en listaDeSemi[0] (max 30) y 
    #  -. lo ancho son la cantidad de valores en listaDeSemi[0].kilogramos[0] (max 25)
    #  -. MzValores[] -> [listaDeSemi[0].id maximo de 30 id de recetas,listaDeSemi[0].kilogramos[0] maxmio 25 valores]
    #     Definiendo el número de filas y columnas
    filas = 40
    columnas = 40
    
    for f in range(filas):
        for c in range(columnas):
            CLX_Cremas.write(f'listaDeSemi[{f}].kilogramos[{c}]', MzValores[f][c])
            # Agregando la celda a la fila
    f = 0 
    for i in listSumaReceta:
        #listaDeSemi[12].SumaKgIng
        CLX_Cremas.write(f'listaDeSemi[{f}].SumaKgIng', float(i))
        print(i)
        f = f +1


