# Import REST FRAMEWORK
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
# Import Django
from django.shortcuts import render
from django.views.generic import ( 
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.models import User
# Local Serializers
from .serializers import (
    RecipesSapSerializer,
    RecipesSapSerializer2,
    RecipesSapSerializer3,
    MaestroDeMaterialesSerializer,
    MaestroDeMaterialesSerializer1,
    MaestroDeMaterialesSerializer2,
    RecetasSerializer,
    RecetasSerializer1,
    RecetasSerializer2,
    RecetasSAPSerializer,
    RecetasSAPSerializer1,
    ProductionOrdersSerializer1,
    ProductionOrdersSerializer2,
    ReporteBatchSerializer,
    ReporteSAPSerializer
    )
# Import datetime  
from datetime import date, datetime, timedelta
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
# Create your views here.
# ********************************************************************************************
# ********************************************************************************************

# List View from Receta SAP in an Url
class RecetasAPI(ListAPIView):
    serializer_class = RecetasSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        return Recetas.objects.all()

# List View from MaestroDeMateriales SAP in an Url
class MaestroDeMaterialesAPI(ListAPIView):
    serializer_class = MaestroDeMaterialesSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return MaestroDeMateriales.objects.all()
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)  

# Create from MaestroDeMateriales SAP in an Url
class CrearMaestroDeMaterialesAPI(CreateAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = MaestroDeMaterialesSerializer1
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Delete from MaestroDeMateriales SAP in an Url
class DeleteMaestroDeMaterialesAPI(DestroyAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = MaestroDeMaterialesSerializer
    # queryset = MaestroDeMateriales.objects.all()
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return MaestroDeMateriales.objects.all()
            #return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)
    
# Deteil_Update from MaestroDeMateriales SAP in an Url
class RetrieveUpdateMaestroDeMaterialesAPI(RetrieveUpdateAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = MaestroDeMaterialesSerializer2
    #queryset = MaestroDeMateriales.objects.all()     
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return MaestroDeMateriales.objects.all()
            #return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# List View from Receta SAP in an Url
class RecetasAPI1(ListAPIView):
    serializer_class = RecetasSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return Recetas.objects.all()
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Detail View from Receta SAP in an Url
class DetailRecetaAPI(ListAPIView):
    serializer_class = RecetasSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            cod_sap = self.kwargs['code']
            return Recetas.objects.recetas_by_id_semielaborado(cod_sap)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Create from Receta SAP in an Url
class CrearRecetaAPI(CreateAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecetasSerializer1
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Delete from Receta SAP in an Url
class DeleteRecetaAPI(DestroyAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecetasSerializer
    #queryset = Recetas.objects.all()    
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return Recetas.objects.all()  
            #return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Deteil_Update from Receta SAP in an Url
class RetrieveUpdateRecetaAPI(RetrieveUpdateAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecetasSerializer2
    #queryset = Recetas.objects.all()
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return Recetas.objects.all()  
            #return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# List View from ReporteBatch SAP in an Url
class ReporteBatchAPI(ListAPIView):
    serializer_class = ReporteBatchSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return ReporteBatch.objects.all()
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# List View from ReporteSAP SAP in an Url
class ReporteSAPAPI(ListAPIView):
    serializer_class = ReporteSAPSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return ReporteSAP.objects.all()
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Detail View from ReporteSAP SAP in an Url
class DetailReporteSAPAPI(ListAPIView):
    serializer_class = ReporteSAPSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            codigo = self.kwargs['code']
            return ReporteSAP.objects.reporte_by_id_turno(codigo)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# List View from ReporteSAP for fecha SAP in an Url
class ListaReporteSAPAPI(ListAPIView):
    serializer_class = ReporteSAPSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            fecha = self.kwargs['fecha']
            dato = datetime.strptime(fecha,"%Y-%m-%d")
            if self.kwargs['fecha'] and dato: return ReporteSAP.objects.reporte_by_datetime_ini(dato)
            else: return Response({'error':' No se envio una fecha valida'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)
            
# List View from ReporteSAP for range fecha SAP in an Url
class ListaReporteSAPAPI1(ListAPIView):
    serializer_class = ReporteSAPSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            fecha1 = self.kwargs['fecha1']
            dato1 = datetime.strptime(fecha1,"%Y-%m-%d %H:%M:%S")
            fecha2 = self.kwargs['fecha2']
            dato2 = datetime.strptime(fecha2,"%Y-%m-%d %H:%M:%S")
            if dato1 and dato2: 
                if dato2 > dato1: return ReporteSAP.objects.reporte_range_datetime_2(dato1,dato2)
                else: return ReporteSAP.objects.reporte_range_datetime_2(dato2,dato1)
            else: return Response({'error':' No se envio fechas validas'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)
# ********************************************************************************************
# ********************************************************************************************
# List View from RecetasSAP in an Url
class ListAllRecetasSAP(ListAPIView):
    serializer_class = RecetasSAPSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        print(usuario)
        print(usuario.is_active)
        # Valido si esta activo el usuario
        if usuario.is_active:
            return RecetasSAP.objects.all()
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Create from Receta SAP in an Url
class CrearRecetaSAP(CreateAPIView):   
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    # Paquete que le da permiso de mostrar o no la informacion
    permission_classes = [IsAuthenticated]
    # Se define el serializador
    serializer_class = RecetasSAPSerializer1
    # Se re-define la funcion create
    def create(self, request, *args, **kwargs):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            # Se serializa la informacion que viene desde el request
            # hacia el formato de serializador que creamos
            serializer = RecetasSAPSerializer1(data=request.data)
            # Verificamos que la data enviada por el request sea valida, si no, finaliza
            serializer.is_valid(raise_exception=True)  # es un if de una sola linea
            # Recupera la informacion de los ingredientes de la receta nueva
            id_s = serializer.validated_data['id_semielaborado']
            ingredientes = serializer.validated_data['ingredientes']
            # Verifico que exista resetas con el mismo semielaborado, para eliminarlas
            id_rest = RecetasSAP.objects.filter(id_semielaborado=id_s)
            # Si existe las elimino 
            id_rest.delete()
            # Ejecuto un for para crear las nuevas recetas SAP
            for ingrediente in ingredientes:
                id_ing = MaestroDeMateriales.objects.get(id=ingrediente['id_ingrediente'])
                id_sem = MaestroDeMateriales.objects.get(id=id_s)
                # Verifico que sean validos los id de semielaborados y de los ingredientes  
                if id_sem and id_ing:
                    receta = RecetasSAP.objects.create(
                        id_semielaborado=id_sem,
                        id_ingrediente=id_ing,
                        valor=ingrediente['value']
                    )
                    receta.save()
            return Response({'mensaje': 'Todo Ok.'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Este usuario no puede iniciar sesion'}, status=status.HTTP_401_UNAUTHORIZED)            

# Delete from Receta SAP in an Url
class DeleteRecetaSAP(ListAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecetasSAPSerializer 

    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            cod_sap = self.kwargs['code']
            # Verifico que exista resetas con el mismo semielaborado, para eliminarlas
            id_rest = RecetasSAP.objects.filter(id_semielaborado=cod_sap)
            # Si existe las elimino
            if id_rest:
                # Las elimino 
                id_rest.delete() 
                return id_rest
                #return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)
   
# List View from ProductionOrders 1 and 2 for range data SAP in an Url
class ReportProductionOrdersSAP(ListAPIView):
    serializer_class = ProductionOrdersSerializer1
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            fecha1 = self.kwargs['fecha1']
            dato1 = datetime.strptime(fecha1,"%Y-%m-%d %H:%M:%S")
            fecha2 = self.kwargs['fecha2']
            dato2 = datetime.strptime(fecha2,"%Y-%m-%d %H:%M:%S")
            if dato1 and dato2: 
                if dato2 > dato1: return ProductionOrders1_SAP.objects.reporte_range_duedate(dato1,dato2)
                else: return ProductionOrders1_SAP.objects.reporte_range_duedate(dato2,dato1)
            else: return Response({'error':' No se envio fechas validas'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Create from ProductionOrders SAP in an Url
class CrearProctuctionOrdersSAP(CreateAPIView):   
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    # Paquete que le da permiso de mostrar o no la informacion
    permission_classes = [IsAuthenticated]
    # Se define el serializador
    serializer_class = ProductionOrdersSerializer2
    # Se re-define la funcion create
    def create(self, request, *args, **kwargs):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            # Se serializa la informacion que viene desde el request
            # hacia el formato de serializador que creamos
            serializer = ProductionOrdersSerializer2(data=request.data)
            # Verificamos que la data enviada por el request sea valida, si no, finaliza
            serializer.is_valid(raise_exception=True)  # es un if de una sola linea
            # Recupera la informacion de los ingredientes de la receta nueva
            itemcodetxt = serializer.validated_data['itemcode']
            wor1 = serializer.validated_data['wor1']
            # Verifico que sea valido el id del semielaborado
            id_sem = MaestroDeMateriales.objects.get(id=itemcodetxt)
            if id_sem:
                order1 = ProductionOrders1_SAP.objects.create(
                    series = serializer.validated_data['series'],
                    itemcode = id_sem,
                    status = serializer.validated_data['status'],
                    type = serializer.validated_data['type'],
                    plannedqty = serializer.validated_data['plannedqty'],
                    postdate = serializer.validated_data['postdate'],
                    startdate = serializer.validated_data['startdate'],
                    duedate = serializer.validated_data['duedate'],
                    comments = serializer.validated_data['comments'],
                    warehouse = serializer.validated_data['warehouse']
                )                                   
                # Creo un nuevo registro en la tabla ProductionOrders1_SAP
                order1.save()
            # Se debe buscar el id o numero del nuevo registro creado en la tabla ProductionOrders1_SAP
            id_order = ProductionOrders1_SAP.objects.get(duedate=serializer.validated_data['duedate'])
            # Ejecuto un for para crear los nuevos registros en la tabla ProductionOrders2_SAP
            for w in wor1:
                # Verifico que sean validos los id de semielaborados y exista un id de la tabla ProductionOrders1_SAP 
                if id_sem and id_order:
                    order2 = ProductionOrders2_SAP.objects.create(
                        parentkey = id_order,
                        linenum = w['linenum'],
                        itemcode = w['itemcode'],
                        plannedqty = w['plannedqty'],
                        issuetype = w['issuetype'],
                        warehouse = w['warehouse'],
                        itemtype = w['itemtype'],
                        stageid = w['stageid']
                    )
                    # Creo unos nuevos registros en la tabla ProductionOrders2_SAP
                    order2.save()
            return Response({'mensaje': 'Todo Ok.'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Este usuario no puede iniciar sesion'}, status=status.HTTP_401_UNAUTHORIZED)            




# ********************************************************************************************
# ********************************************************************************************
# Create your views here.
# Lista todas las recetas de la empresa en una HTML
class ListAllRecipesSAP(ListView):
    template_name = 'api/list_all.html'
    paginate_by = 20
    ordering = 'code'
    #model = RecipesSAP # Se elimina si se usa el metod get
    # Se puede usar una variable de contexto en vez de usar en pantalla el "object_list"
    #context_object_name = 'list_all'

    def get_queryset(self):
    # Codigo que filtra lista de recetas desde la pantalla
    # El 'self.request.GET.get' nos permite recoger una variable desde el HTML
    # desde un <input> y un <button>
        clave = self.request.GET.get('kword', '')
        lista = RecipesSAP.objects.filter(
            name__icontains=clave)
        return lista
# ********************************************************************************************
# ********************************************************************************************
# List View from Recipes SAP in an Url
class ListRecipesSAP(ListAPIView):
    serializer_class = RecipesSapSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        # print('****************************')
        # print(self.request.user)
        # print('****************************')
        usuario = self.request.user
        # print(usuario.id)
        # print(usuario.is_active)
        # print('****************************')
        # Valido si esta activo el usuario
        if usuario.is_active:
            return RecipesSAP.objects.all()
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Detail View from Recipes SAP in an Url
class DetailRecipeSAP(ListAPIView):
    serializer_class = RecipesSapSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            cod_sap = self.kwargs['code']
            return RecipesSAP.objects.recipe_by_code(cod_sap)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Detail View from Recipes SAP in an Url
class DetailRecipeSAP2(ListAPIView):
    serializer_class = RecipesSapSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            cod_sap = self.request.query_params.get('code', None)
            return RecipesSAP.objects.recipe_by_code(cod_sap)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Create from Recipe SAP in an Url
#class CreateRecipeSAP(CreateAPIView):
#     serializer_class = RecipesSapSerializer2

# Create from Recipe SAP in an Url
class CreateRecipeSAP(CreateAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecipesSapSerializer2
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            return Response({'mensaje':'Todo Ok.'}, status = status.HTTP_200_OK)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)

# Detail from Recipe SAP in an Url
class DetailRecipeSAP3(RetrieveAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecipesSapSerializer
    queryset = RecipesSAP.objects.filter() # Puedes usar 'all'

# Delete from Recipe SAP in an Url
class DeleteRecipeSAP(DestroyAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecipesSapSerializer
    queryset = RecipesSAP.objects.all()

# Update from Recipe SAP in an Url
class UpdateRecipeSAP(UpdateAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecipesSapSerializer3
    queryset = RecipesSAP.objects.all()

# Deteil_Update from Recipe SAP in an Url
class RetrieveUpdateRecipeSAP(RetrieveUpdateAPIView):
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    serializer_class = RecipesSapSerializer3
    queryset = RecipesSAP.objects.all()
