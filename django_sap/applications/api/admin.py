from django.contrib import admin

# Register your models here.
from .models import (
    RecipesSAP, 
    Ingredientes, 
    Semielaborados, 
    ReporteBatch, 
    ReporteSAP, 
    Recetas, 
    MaestroDeMateriales, 
    RecetasSAP,
    ProductionOrders1_SAP,
    ProductionOrders2_SAP,
    operaciones,
    em_sp
)
# Defino los titulos de las columnas de el admin. de Django
class MaestroDeMaterialesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type'
        )
    search_fields =(
        'id',
        'name',
        'type'
    )
    # Permite ordenar por una o mas columnas
    ordering = (
        'id',
    )
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('id',)

admin.site.register(MaestroDeMateriales,MaestroDeMaterialesAdmin)

""" class RecetasAdmin(admin.ModelAdmin):
    list_display = (
        'id_semielaborado',
        )
    # Permite ordenar por una o mas columnas
    ordering = ('id_semielaborado',)
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('id_semielaborado',)

admin.site.register(Recetas,RecetasAdmin) """

class ReporteBatchAdmin(admin.ModelAdmin):
    list_display = (
        'nro_batch',
        'id_lote',
        'id_turno',
        'id_semielaborado',
        )
    search_fields =(
        'nro_batch',
        'id_lote',
        'id_turno',
        'id_semielaborado',
    )
    # Permite ordenar por una o mas columnas
    ordering = ('nro_batch',)
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('nro_batch',)

admin.site.register(ReporteBatch,ReporteBatchAdmin)

""" class ReporteSAPAdmin(admin.ModelAdmin):
    list_display = (
        'id_turno',
        'id_semielaborado',
        'datetime_ini',
        )
    search_fields =(
        'id_turno',
        'id_semielaborado',
        'datetime_ini',
        )
    # Permite ordenar por una o mas columnas
    ordering = ('id_turno',)
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('id_turno',)

admin.site.register(ReporteSAP,ReporteSAPAdmin) """


###########################################################################
###########################################################################

class RecetasSAPAdmin(admin.ModelAdmin):
    list_display = (
        'id_semielaborado',
        'id_ingrediente',
        'valor',
        )
    search_fields =(
       'id_semielaborado',
       'id_ingrediente',
        )
    #search_fields = ['id_semielaborado']

    # Permite ordenar por una o mas columnas
    ordering = ('id_semielaborado', )
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('id_semielaborado',)

admin.site.register(RecetasSAP,RecetasSAPAdmin)

class ProductionOrders1_SAPAdmin(admin.ModelAdmin):
    list_display = (
        'docentry',
        'series',
        'itemcode',
        'plannedqty',
        'comments'
        )
    search_fields =(
        'docentry',
        'series',
        'itemcode',
    )
    # Permite ordenar por una o mas columnas
    ordering = ('docentry',)
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('docentry',)

admin.site.register(ProductionOrders1_SAP,ProductionOrders1_SAPAdmin)

class ProductionOrders2_SAPAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'parentkey',
        'linenum',
        'itemcode',
        'plannedqty',
        )
    search_fields =(
        'parentkey',
        'linenum',
        'itemcode',
    )
    # Permite ordenar por una o mas columnas
    ordering = ('-parentkey','linenum')
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('parentkey',)

admin.site.register(ProductionOrders2_SAP,ProductionOrders2_SAPAdmin)


#@admin.site.register(operaciones)

class operacionesAdmin(admin.ModelAdmin):
    list_display = (
        'hora',
        'idlote',
        'hora_fin',
        'receta_total_kg',
        'em1',
        'em2',
        'em3',
        'em4',
        'em5',
        'em6',
        'em7',
        'em8'
        )
    search_fields =(
        'hora',
    )
    # Permite ordenar por una o mas columnas
    ordering = (
        '-hora',
    )
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('hora','idlote')

admin.site.register(operaciones,operacionesAdmin)

class em_spAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'em',
        'ID',
        'Ingrediente',
        'SP'
        )
    search_fields =(
        'em',
        'ID',
        'Ingrediente',
        'SP'
    )
    # Permite ordenar por una o mas columnas
    ordering = (
        'em',
    )
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('ID','Ingrediente')

admin.site.register(em_sp,em_spAdmin)
