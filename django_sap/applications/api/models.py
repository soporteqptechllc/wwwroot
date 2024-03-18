# Import Model Django
from django.db import models

# Local Managers
from .managers import (
   RecipeManager, 
   ReporteSAPManager, 
   RecetasManager, 
   RecetasSAPManager, 
   ProductionOrders1Manager, 
   ProductionOrders2Manager
)

# Create your models here.
class Ingredientes(models.Model):
    id = models.CharField('id_Ingrediente', max_length=50, unique=True, primary_key=True)
    name = models.CharField('name_Ingrediente', max_length=60, unique=True)
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Ingrediente'  # Nombre de Columna singular
      verbose_name_plural = 'Ingredientes'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id) + ' - ' + self.name


class Semielaborados(models.Model):
    id = models.CharField('id_Semielaborado', max_length=50, unique=True, primary_key=True)
    name = models.CharField('name_Semielaborado', max_length=50, unique=True)
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Semielaborado'  # Nombre de Columna singular
      verbose_name_plural = 'Semielaborados'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id) + ' - ' + self.name

class MaestroDeMateriales(models.Model):
    id = models.CharField('id_MaestroDeMateriales', max_length=50, unique=True, primary_key=True)
    name = models.CharField('name_MaestroDeMateriales', max_length=50, unique=True)
    type = models.CharField('type_MaestroDeMateriales', max_length=50)
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'MaestroDeMaterial'  # Nombre de Columna singular
      verbose_name_plural = 'MaestroDeMateriales'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      #return str(self.id) + ' - ' + self.name + ' - ' + self.type
      return str(self.id)

class ReporteBatch(models.Model):
    nro_batch =models.IntegerField('NroBatch', unique=True, primary_key=True)
    id_lote = models.CharField('id_Lote', max_length=50, unique=True)
    id_turno = models.IntegerField('id_Turno', unique=True)
    id_semielaborado = models.ForeignKey(MaestroDeMateriales, on_delete=models.CASCADE, related_name='id_semielaborado')
    datetime_ini = models.DateTimeField('datatime_Ini', blank=True, null=True)
    datetime_end = models.DateTimeField('datatime_End', blank=True, null=True)
    id_ingrediente = models.ForeignKey(MaestroDeMateriales, on_delete=models.CASCADE, related_name='id_ingrediente', null=True)
    kg_teorico = models.DecimalField('Kg_Teorico', max_digits=10, decimal_places=2)
    Kg_real = models.DecimalField('Kg_Real', max_digits=10, decimal_places=2)
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'ReporteBatch'  # Nombre de Columna singular
      verbose_name_plural = 'ReportesBatchs'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.nro_batch) + ' - ' + str(self.id_lote) + ' - ' + str(self.id_turno)

class ReporteSAP(models.Model):
    id_turno = models.IntegerField('id_Turno', unique=True)
    id_semielaborado = models.ForeignKey(MaestroDeMateriales, on_delete=models.CASCADE)
    datetime_ini = models.DateTimeField('datatime_Ini', blank=True, null=True)
    datetime_end = models.DateTimeField('datatime_End', blank=True, null=True)
    cantidad_batch = models.IntegerField('cantidad_Batch', unique=True)
    kg_total_seimielaborado = models.DecimalField(
        'kg_total_seimielaborado', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000009 = models.DecimalField(
        'Kg_Tot_MPC000009', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000022 = models.DecimalField(
        'Kg_Tot_MPC000022', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000025 = models.DecimalField(
        'Kg_Tot_MPC000025', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000027 = models.DecimalField(
        'Kg_Tot_MPC000027', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000029 = models.DecimalField(
        'Kg_Tot_MPC000029', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000030 = models.DecimalField(
        'Kg_Tot_MPC000030', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000033 = models.DecimalField(
        'Kg_Tot_MPC000033', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )    
    Kg_Tot_MPC000035 = models.DecimalField(
        'Kg_Tot_MPC000035', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000037 = models.DecimalField(
        'Kg_Tot_MPC000037', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPC000038 = models.DecimalField(
        'Kg_Tot_MPC000038', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPCL00002 = models.DecimalField(
        'Kg_Tot_MPCL00002', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPCL00008 = models.DecimalField(
        'Kg_Tot_MPCL00008', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPCL00011 = models.DecimalField(
        'Kg_Tot_MPCL00011', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPCL00013 = models.DecimalField(
        'Kg_Tot_MPCL00013', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPD000044 = models.DecimalField(
        'Kg_Tot_MPD000044', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPD000002 = models.DecimalField(
        'Kg_Tot_MPD000002', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPD000004 = models.DecimalField(
        'Kg_Tot_MPD000004', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPD000008 = models.DecimalField(
        'Kg_Tot_MPD000008', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPJ000017 = models.DecimalField(
        'Kg_Tot_MPJ000017', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPJ000018 = models.DecimalField(
        'Kg_Tot_MPJ000018', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPL000038 = models.DecimalField(
        'Kg_Tot_MPL000038', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPL000048 = models.DecimalField(
        'Kg_Tot_MPL000048', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    Kg_Tot_MPL000065 = models.DecimalField(
        'Kg_Tot_MPL000065', 
        max_digits=10, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    # Importo modelos avanzados de Manager
    objects = ReporteSAPManager() 
      
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'ReporteSAP'  # Nombre de Columna singular
      verbose_name_plural = 'ReportesSAP'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id_turno) + ' - ' + str(self.id_semielaborado) + ' - ' + str(self.datetime_ini)

class Recetas(models.Model):
    id_semielaborado = models.OneToOneField(MaestroDeMateriales, on_delete=models.CASCADE, primary_key=True)
    MPC000009 = models.DecimalField(
        'MPC000009', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000022 = models.DecimalField(
        'MPC000022', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000025 = models.DecimalField(
        'MPC000025', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000027 = models.DecimalField(
        'MPC000027', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000029 = models.DecimalField(
        'MPC000029', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000030 = models.DecimalField(
        'MPC000030', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000033 = models.DecimalField(
        'MPC000033', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )    
    MPC000035 = models.DecimalField(
        'MPC000035', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000037 = models.DecimalField(
        'MPC000037', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPC000038 = models.DecimalField(
        'MPC000038', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPCL00002 = models.DecimalField(
        'MPCL00002', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPCL00008 = models.DecimalField(
        'MPCL00008', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPCL00011 = models.DecimalField(
        'MPCL00011', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPCL00013 = models.DecimalField(
        'MPCL00013', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPD000044 = models.DecimalField(
        'MPD000044', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPDC00002 = models.DecimalField(
        'MPDC00002', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPDC00004 = models.DecimalField(
        'MPDC00004', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPDC00008 = models.DecimalField(
        'MPDC00008', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPJ000017 = models.DecimalField(
        'MPJ000017', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPJ000018 = models.DecimalField(
        'MPJ000018', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPL000038 = models.DecimalField(
        'MPL000038', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPL000048 = models.DecimalField(
        'MPL000048', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    MPL000065 = models.DecimalField(
        'MPL000065', 
        max_digits=6, 
        decimal_places=3, 
        default=0,
        blank=True, null=True
    )
    # Importo modelos avanzados de Manager
    objects = RecetasManager() 
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Receta'  # Nombre de Columna singular
      verbose_name_plural = 'Recetas'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id_semielaborado)

"""Modelo de la tabla de la BD Habilidades"""
class RecipesSAP(models.Model):
    name = models.CharField('RecipeName', max_length=50, unique=True)
    description = models.CharField('Description', max_length=100, blank=True, null=True)
    code = models.CharField('CodeSAP', max_length=50, unique=True, primary_key=True)
    ingredient1 = models.CharField('IngredientName1', max_length=50, default='SULFATO (Kg)')
    tag_plc1 = models.CharField('TagSet1', max_length=50, default='[Cremas]EM1_W1_SP')
    value1 = models.DecimalField(
        'RecipeValue1', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient2 = models.CharField('IngredientName2', max_length=50, default='CARBONATO1 (Kg)')
    tag_plc2 = models.CharField('TagSet2', max_length=50, default='[Cremas]EM2_W1_SP')
    value2 = models.DecimalField(
        'RecipeValue2', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient3 = models.CharField('IngredientName3', max_length=50, default='CARBONATO2 (Kg)')
    tag_plc3 = models.CharField('TagSet3', max_length=50, default='[Cremas]EM3_W1_SP')
    value3 = models.DecimalField(
        'RecipeValue3', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient4 = models.CharField('IngredientName4', max_length=50, default='CARBONATO3 (Kg)')
    tag_plc4 = models.CharField('TagSet4', max_length=50, default='[Cremas]EM4_W1_SP')
    value4 = models.DecimalField(
        'RecipeValue4', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient5 = models.CharField('IngredientName5', max_length=50, default='TRIPOLI (Kg)')
    tag_plc5 = models.CharField('TagSet5', max_length=50, default='[Cremas]EM5_W1_SP')
    value5 = models.DecimalField(
        'RecipeValue5', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient6 = models.CharField('IngredientName6', max_length=50, default='AGUA (Kg)')
    tag_plc6 = models.CharField('TagSet6', max_length=50, default='[Cremas]EM6_W1_SP')
    value6 = models.DecimalField(
        'RecipeValue6', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient7 = models.CharField('IngredientName7', max_length=50, default='LABSA (Kg)')
    tag_plc7 = models.CharField('TagSet7', max_length=50, default='[Cremas]EM7_W1_SP')
    value7 = models.DecimalField(
        'RecipeValue7', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient8 = models.CharField('IngredientName8', max_length=50, default='DEA (Kg)')
    tag_plc8 = models.CharField('TagSet8', max_length=50, default='[Cremas]EM8_W1_SP')
    value8 = models.DecimalField(
        'RecipeValue8', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    ingredient9 = models.CharField('IngredientName9', max_length=50, default='BUTIL (Kg)')
    tag_plc9 = models.CharField('TagSet9', max_length=50, default='[Cremas]EM9_W1_SP')
    value9 = models.DecimalField(
        'RecipeValue9', 
        max_digits=6, 
        decimal_places=3, 
        default=0
    )
    # Importo modelos avanzados de Manager
    objects = RecipeManager()

    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Recipe'  # Nombre de Columna singular
      verbose_name_plural = 'Recipes'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.code) + ' - ' + self.name


 ####################################################################################
 ####################################################################################
 # Receta SAP para ser cargada por URL de REST API   
class RecetasSAP(models.Model):

    id_semielaborado = models.ForeignKey(MaestroDeMateriales, on_delete=models.CASCADE, related_name='id_Semielaborado')
    id_ingrediente = models.ForeignKey(MaestroDeMateriales, on_delete=models.CASCADE, related_name='id_Ingrediente')
    valor = models.DecimalField(
        'valor', 
        max_digits=10, 
        decimal_places=8,
        default=0
    )
    # Importo modelos avanzados de Manager
    objects = RecetasSAPManager()

    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'RecetaSAP'  # Nombre de Columna singular
      verbose_name_plural = 'RecetasSAP'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id)
    

######################################################
######################################################
# Tabla de Informacion General del Reporte SAP
class ProductionOrders1_SAP(models.Model):
       
    docentry = models.BigAutoField(primary_key=True)
    series = models.IntegerField('Series')
    itemcode = models.ForeignKey(MaestroDeMateriales, on_delete=models.CASCADE, related_name='ProductNo')
    status = models.CharField('ProductionOrderStatus', max_length=30, blank=True, null=True)
    type = models.CharField('Type', max_length=1, blank=True, null=True)
    plannedqty = models.DecimalField(
        'PlannedQty', 
        max_digits=40, 
        decimal_places=6, 
        default=0,
        blank=True, null=True
    )
    postdate = models.DateTimeField('OrderDate', blank=True, null=True)
    startdate = models.DateTimeField('StartDate', blank=True, null=True)
    duedate = models.DateTimeField('DueDate', blank=True, null=True)
    comments = models.CharField('Remarks', max_length=254, blank=True, null=True)
    warehouse = models.CharField('Warehouse', max_length=8, blank=True, null=True)

    # Importo modelos avanzados de Manager
    objects = ProductionOrders1Manager() 
      
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'ProductionOrder1'  # Nombre de Columna singular
      verbose_name_plural = 'ProductionOrders1'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.docentry)

# Tabla de Informacion Detallada del Reporte SAP
class  ProductionOrders2_SAP(models.Model):

    parentkey = models.ForeignKey(ProductionOrders1_SAP, on_delete=models.CASCADE, related_name='ParentKey')
    linenum = models.IntegerField('LineNum')
    itemcode = models.ForeignKey(MaestroDeMateriales, on_delete=models.CASCADE, related_name='ItemNo')
    plannedqty = models.DecimalField(
        'PlannedQty', 
        max_digits=40, 
        decimal_places=6, 
        default=0,
        blank=True, null=True
    )
    issuetype = models.CharField('ProductionOrderIssueType', max_length=30, blank=True, null=True)
    warehouse = models.CharField('Warehouse', max_length=8, blank=True, null=True)
    itemtype = models.IntegerField('ItemType', blank=True, null=True)
    stageid = models.IntegerField('StageId', blank=True, null=True)
    
    # Importo modelos avanzados de Manager
    objects = ProductionOrders2Manager() 
      
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'ProductionOrder2'  # Nombre de Columna singular
      verbose_name_plural = 'ProductionOrders2'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.parentkey) + ' - ' + str(self.linenum) + ' - ' + str(self.itemcode)
    
# Tabla de Encabezado del reporte de Produccion por turno datos generales de los batch


# Tabla del detalle de por turno batch a batch
class operaciones(models.Model):
   idlote = models.BigIntegerField('idlote',blank=True, null=True)
   receta_id = models.CharField('receta_id',max_length=50, blank=True, null=True)
   receta_nombre = models.CharField('receta_nombre',max_length=50, blank=True, null=True)
   receta_total_kg = models.FloatField('receta_total_kg', blank=True, null=True)
   receta_total_set_kg = models.FloatField('receta_total_set_kg', blank=True, null=True)
   idfabricacion = models.BigIntegerField('idfabricacion',blank=True, null=True) # año, mes, hora, minuto, y segundos. solo cuando se realizo el reporte
   humedad = models.FloatField('humedad', blank=True, null=True)
   ph = models.FloatField('ph', blank=True, null=True)
   hora = models.CharField('hora',max_length=20, blank=True, null=True)
   hora_fin = models.CharField('hora_fin',max_length=20, blank=True, null=True)
   em1_time = models.CharField('em1_time',max_length=20, blank=True, null=True)
   em1 = models.FloatField('em1', blank=True, null=True)
   em2_time = models.CharField('em2_time',max_length=20, blank=True, null=True)
   em2 = models.FloatField('em2', blank=True, null=True)
   em3_time = models.CharField('em3_time',max_length=20, blank=True, null=True)
   em3 = models.FloatField('em3', blank=True, null=True)
   em4_time = models.CharField('em4_time',max_length=20, blank=True, null=True)
   em4 = models.FloatField('em4', blank=True, null=True)
   em5_time = models.CharField('em5_time',max_length=20, blank=True, null=True)
   em5 = models.FloatField('em5', blank=True, null=True)
   em6_time = models.CharField('em6_time',max_length=20, blank=True, null=True)
   em6 = models.FloatField('em6', blank=True, null=True)
   em7_time = models.CharField('em7_time',max_length=20, blank=True, null=True)
   em7 = models.FloatField('em7', blank=True, null=True)
   em8_time = models.CharField('em8_time',max_length=20, blank=True, null=True)
   em8 = models.FloatField('em8', blank=True, null=True)
   em9_time = models.CharField('em9_time',max_length=20, blank=True, null=True)
   em9 = models.FloatField('em9', blank=True, null=True)
   em10_time = models.CharField('em10_time',max_length=20, blank=True, null=True)
   em10 = models.FloatField('em10', blank=True, null=True)
   em11_time = models.CharField('em11_time',max_length=20, blank=True, null=True)
   em11 = models.FloatField('em11', blank=True, null=True)
   em12_time = models.CharField('em12_time',max_length=20, blank=True, null=True)
   em12 = models.FloatField('em12', blank=True, null=True)
   em13_time = models.CharField('em13_time',max_length=20, blank=True, null=True)
   em13 = models.FloatField('em13', blank=True, null=True)
   em14_time = models.CharField('em14_time',max_length=20, blank=True, null=True)
   em14 = models.FloatField('em14', blank=True, null=True)
   em15_time = models.CharField('em15_time',max_length=20, blank=True, null=True)
   em15 = models.FloatField('em15', blank=True, null=True)
   em16_time = models.CharField('em16_time',max_length=20, blank=True, null=True)
   em16 = models.FloatField('em16', blank=True, null=True)
   em17_time = models.CharField('em17_time',max_length=20, blank=True, null=True)
   em17 = models.FloatField('em17', blank=True, null=True)
   em18_time = models.CharField('em18_time',max_length=20, blank=True, null=True)
   em18 = models.FloatField('em18', blank=True, null=True)
   em19_time = models.CharField('em19_time',max_length=20, blank=True, null=True)
   em19 = models.FloatField('em19', blank=True, null=True)
   em20_time = models.CharField('em20_time',max_length=20, blank=True, null=True)
   em20 = models.FloatField('em20', blank=True, null=True)
   em21_time = models.CharField('em21_time',max_length=20, blank=True, null=True)
   em21 = models.FloatField('em21', blank=True, null=True)
    # Funciones adicional para calcular los totales de Kg
    # Busca la descripcion de la receta por su id
   def save(self, *args, **kwargs):
      # Calcular el total
      total = 0
      if self.em1:
         total = total + self.em1
      if self.em2:
         total = total + self.em2
      if self.em3:
         total = total + self.em3
      if self.em4:
         total = total + self.em4
      if self.em5:
         total = total + self.em5
      if self.em6:
         total = total + self.em6
      if self.em7:
         total = total + self.em7
      if self.em8:
         total = total + self.em8
      if self.em9:
         total = total + self.em9
      if self.em10:
         total = total + self.em10
      if self.em11:
         total = total + self.em11
      if self.em12:
         total = total + self.em12
      if self.em13:
         total = total + self.em13
      if self.em14:
         total = total + self.em14
      if self.em15:
         total = total + self.em15
      if self.em16:
         total = total + self.em16
      if self.em17:
         total = total + self.em17
      if self.em18:
         total = total + self.em18
      if self.em19:
         total = total + self.em19
      if self.em20:
         total = total + self.em20
      if self.em21:
         total = total + self.em21

      self.receta_total_kg = total                             
      # Buscar la descripcion 
      DesSem = ""                            
      if self.receta_id:
         Maestro = MaestroDeMateriales.objects.filter(id = self.receta_id).values()

         if Maestro:
            DesSem = Maestro[0]['name']

      self.receta_nombre = DesSem    

      super(operaciones,self).save(*args,**kwargs)

class em_sp(models.Model):
   em   = models.IntegerField('em',blank=True,null=True)
   ID   = models.CharField('ID_ingrediente',max_length=20, blank=True,null=True)
   Ingrediente = models.CharField('Ingrediente',max_length=20, blank=True,null=True)
   SP = models.FloatField('sp', blank=True, null=True)
