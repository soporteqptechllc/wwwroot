# Import REST FRAMEWORK
from rest_framework import serializers
# Local Models de la BD
from .models import (
    RecipesSAP, 
    Recetas, 
    MaestroDeMateriales, 
    ReporteBatch, 
    ReporteSAP, 
    RecetasSAP,
    ProductionOrders1_SAP,
    ProductionOrders2_SAP, 
)

# Serializador de MaestroDeMateriales
class MaestroDeMaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaestroDeMateriales
        fields = ('__all__')

# Serializador de MaestroDeMateriales
class MaestroDeMaterialesSerializer1(serializers.ModelSerializer):
    class Meta:
        model = MaestroDeMateriales
        fields = (
            'id',
            'name',
            'type',
            )

# Serializador de MaestroDeMateriales
class MaestroDeMaterialesSerializer2(serializers.ModelSerializer):
    class Meta:
        model = MaestroDeMateriales
        fields = (
            'name',
            'type',
            )

# Serializador de Receta
class RecetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = ('__all__')

# Serializador de Receta
class RecetasSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = (
            'id_semielaborado',
            'MPC000009',
            'MPC000022',
            'MPC000025',
            'MPC000027',
            'MPC000029',
            'MPC000030',
            'MPC000033',
            'MPC000035',
            'MPC000037',
            'MPC000038',
            'MPCL00002',
            'MPCL00008',
            'MPCL00011',
            'MPCL00013',
            'MPD000044',
            'MPDC00002',
            'MPDC00004',
            'MPDC00008',
            'MPJ000017',
            'MPJ000018',
            'MPL000038',
            'MPL000048',
            'MPL000065',
        )
# Serializador de Receta
class RecetasSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = (
            'MPC000009',
            'MPC000022',
            'MPC000025',
            'MPC000027',
            'MPC000029',
            'MPC000030',
            'MPC000033',
            'MPC000035',
            'MPC000037',
            'MPC000038',
            'MPCL00002',
            'MPCL00008',
            'MPCL00011',
            'MPCL00013',
            'MPD000044',
            'MPDC00002',
            'MPDC00004',
            'MPDC00008',
            'MPJ000017',
            'MPJ000018',
            'MPL000038',
            'MPL000048',
            'MPL000065',
        )
# Serializador de ReporteBatch
class ReporteBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteBatch
        fields = ('__all__')

# Serializador de ReporteSAP
class ReporteSAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteSAP
        fields = ('__all__')
# *******************************************************
# *******************************************************
# Serializador de Recipes SAP
class RecipesSapSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipesSAP
        #fields = ('__all__')
        fields = (
            'name',
            'description',
            'code',
            'ingredient1',
            'value1',
            'ingredient2',
            'value2',
            'ingredient3',
            'value3',
            'ingredient4',
            'value4',
            'ingredient5',
            'value5',
            'ingredient6',
            'value6',
            'ingredient7',
            'value7',
            'ingredient8',
            'value8',
            'ingredient9',
            'value9',                                           
        )
class RecipesSapSerializer2(serializers.ModelSerializer):
    class Meta:
        model = RecipesSAP
        fields = (
            'name',
            'description',
            'code',
            'value1',
            'value2',
            'value3',
            'value4',
            'value5',
            'value6',
            'value7',
            'value8',
            'value9',                                           
        )
class RecipesSapSerializer3(serializers.ModelSerializer):
    class Meta:
        model = RecipesSAP
        fields = (
            'value1',
            'value2',
            'value3',
            'value4',
            'value5',
            'value6',
            'value7',
            'value8',
            'value9',                                           
        )

# *******************************************************
# *******************************************************

# Serializadores para la RecetaSAP
class RecetasSAPDetailSerializer(serializers.Serializer):

        id_ingrediente = serializers.CharField()     
        value = serializers.DecimalField(
        max_digits=10, 
        decimal_places=8, 
    )

class RecetasSAPSerializer1(serializers.Serializer):

    id_semielaborado = serializers.CharField()
    ingredientes = RecetasSAPDetailSerializer(many = True)


class RecetasSAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetasSAP
        fields = ('__all__')

# *******************************************************
# *******************************************************

# Serializadores para la ProductionOrders 1 y 2
class ProductionOrdersSerializer1(serializers.ModelSerializer):
    wor1 = serializers.SerializerMethodField()
    class Meta:
        model = ProductionOrders1_SAP
        ordering = ['docentry']
        fields = (
            'docentry',
            'series',
            'itemcode',
            'status',
            'type',
            'plannedqty',
            'postdate',
            'startdate',
            'duedate',
            'comments',
            'warehouse',
            'wor1',
            )
    # Realiza una busqueda de los detalles de la venta con el id del "objecto" del URL
    def get_wor1(self, obj):
        query = ProductionOrders2_SAP.objects.order_by_parentkey(obj.docentry)
        wor1_serializados =DetalleVentaProductoSerializer(query, many = True).data
        return wor1_serializados
            
class DetalleVentaProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductionOrders2_SAP
        fields = (
            'parentkey',
            'linenum',
            'itemcode',
            'plannedqty',
            'issuetype',
            'warehouse',
            'itemtype',
            'stageid',
        )
class DetalleVentaProductoSerializer2(serializers.ModelSerializer):

    class Meta:
        model = ProductionOrders2_SAP
        fields = (
            'linenum',
            'itemcode',
            'plannedqty',
            'issuetype',
            'warehouse',
            'itemtype',
            'stageid',
        )
             
class ProductionOrdersSerializer2(serializers.Serializer):
    
    series = serializers.IntegerField()
    itemcode = serializers.CharField()
    status = serializers.CharField()
    type = serializers.CharField()
    plannedqty = serializers.DecimalField( 
        max_digits=40, 
        decimal_places=2, 
    )
    postdate = serializers.DateTimeField()
    startdate = serializers.DateTimeField()
    duedate = serializers.DateTimeField()
    comments = serializers.CharField()
    warehouse = serializers.CharField()
    wor1 = DetalleVentaProductoSerializer2(many = True)

