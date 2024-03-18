"""
URLS DE EL APP API REST
"""
# Django
from django.urls import path
# Local
from . import views

app_name = 'api_app'
urlpatterns = [
     # URL - Lista de maestrodemateriales en general
     path('api/api/lista_maestrodemateriales/', 
          views.MaestroDeMaterialesAPI.as_view(), name='maestrodemateriales-lista'),
     # URL - Creacion de maestrodemateriales
     path('api/api/crear-maestrodemateriales/',
         views.CrearMaestroDeMaterialesAPI.as_view(), name='maestrodemateriales_create'),
     # URL - Borrado de maestrodemateriales
     path('api/api/borrar-maestrodemateriales/<pk>/',
         views.DeleteMaestroDeMaterialesAPI.as_view(), name='maestrodemateriales_delete'),
     # URL - Actualizacion de maestrodemateriales  
     path('api/api/detail-update-maestrodemateriales/<pk>/',
         views.RetrieveUpdateMaestroDeMaterialesAPI.as_view(), name='maestrodemateriales-detail_update'),

     # URL - Lista de recetas en general
     path('api/api/listar_todas_recetas/', 
          views.RecetasAPI.as_view(), name='recetas_all'),
     # URL - Lista de recetas en general
     path('api/api/lista-recetas/',
         views.RecetasAPI1.as_view(), name='recetas-lista'),
     # URL - Detalle de receta por codigo sap
     path('api/api/detalle-receta/<code>/',
         views.DetailRecetaAPI.as_view(), name='receta_by_code'),
     # URL - Creacion de receta
     path('api/api/crear-receta/',
         views.CrearRecetaAPI.as_view(), name='receta_create'),
     # URL - Borrado de receta
     path('api/api/borrar-receta/<pk>/',
         views.DeleteRecetaAPI.as_view(), name='receta_delete'),
     # URL - Actualizacion de receta
     path('api/api/detail-update-receta/<pk>/',
         views.RetrieveUpdateRecetaAPI.as_view(), name='receta-detail_update'),

     # ******************************************************
     # ******************************************************
    # RECETAS SAP
     # URL - Lista de recetas en general
     path('api/api/lista-recetas-sap/',
         views.ListAllRecetasSAP.as_view(), name='recetassap-lista'),
     # URL - Creacion de recetaSAP
     path('api/api/crear-receta-sap/',
          views.CrearRecetaSAP.as_view(), name='recetasap_create'),
         # URL - Borrado de receta
     path('api/api/borrar-receta-sap/<code>/',
         views.DeleteRecetaSAP.as_view(), name='recetasap_delete'),
     # ****************************************************** 
     # ****************************************************** 
     # URL - Lista de reportebatch en general
     path('api/api/lista_reportebatch/', 
          views.ReporteBatchAPI.as_view(), name='reportebatch-lista'),
     # URL - Lista de reportesap en general
     path('api/api/lista_reportesap/', 
          views.ReporteSAPAPI.as_view(), name='reportesap-lista'),
     # URL - Detalle de reportesap por codigo
     path('api/api/detalle-reportesap/<code>/',
         views.DetailReporteSAPAPI.as_view(), name='reportesap_by_code'),
     # URL - lista de reportesap por fecha
     path('api/api/lista-fecha-reportesap/<fecha>/',
         views.ListaReporteSAPAPI.as_view(), name='reportesap_by_fecha'),
     # URL - lista de reportesap por fecha
     path('api/api/rango-fecha-reportesap/<fecha1>/<fecha2>/',
         views.ListaReporteSAPAPI1.as_view(), name='reportesap_range_fecha'),
    # URL - lista de reportesap por fecha
     path('api/api/rango-fecha-reportproductionorders/<fecha1>/<fecha2>/',
         views.ReportProductionOrdersSAP.as_view(), name='reportproductionorders_range_fecha'),
    # URL - Creacion de Reporte SAP de Ordenes de Produccion
     path('api/api/crear-productionorders-sap/',
          views.CrearProctuctionOrdersSAP.as_view(), name='productionorders_create'),        
     # ****************************************************** 
     # ******************************************************  
    # URL - Detalle de receta por codigo sap
     path('api/api/detalle-recetax/<code>/',
         views.DetailRecipeSAP.as_view(), name='api-recipe_by_code'),
    # URL - Detalle de receta por codigo sap
     path('api/api/detalle-receta2/',
         views.DetailRecipeSAP2.as_view(), name='api-recipe_by_code2'),
    path('api/api/detalle-receta3/<pk>/',
         views.DetailRecipeSAP3.as_view(), name='api-recipe_by_cpk'),    
    # URL - Creacion de receta
     path('api/api/create-sap/',
         views.CreateRecipeSAP.as_view(), name='api-recipe_create'),
    # URL - Borrado de receta
    path('api/api/delete-sap/<pk>/',
         views.DeleteRecipeSAP.as_view(), name='api-recipe_delete'),
    # URL - Actualizacion de receta
    path('api/api/update-sap/<pk>/',
         views.UpdateRecipeSAP.as_view(), name='api-recipe_update'),
    # URL - Actualizacion de receta
    path('api/api/detail-update/<pk>/',
         views.RetrieveUpdateRecipeSAP.as_view(), name='api-detail_update'),                  
]