# Import Django
from django.db import models

# models avanzados
class RecipeManager(models.Manager):
    
    def recipe_by_code(self,codigo):
        return self.filter(
            code = codigo
        )

class ReporteSAPManager(models.Manager):
    
    def reporte_by_id_turno(self,idturno):
        return self.filter(
            id_turno = idturno
        )
    def reporte_by_datetime_ini(self,fecha):
        return self.filter(
            datetime_ini__gte = fecha
        )
    # Estos 2 metodos son iguales en el resultado
    def reporte_range_datetime_1(self,fecha1,fecha2):
        return self.filter(
            datetime_ini__range = (fecha1,fecha2)
            )
    def reporte_range_datetime_2(self,fecha1,fecha2):
        return self.filter(datetime_ini__gte = fecha1).filter(datetime_ini__lte = fecha2)


class RecetasManager(models.Manager):
    
    def recetas_by_id_semielaborado(self,codigo):
        return self.filter(
            id_semielaborado = codigo
        )

class RecetasSAPManager(models.Manager):
    
    def recetas_by_id_semielaborado(self,codigo):
        return self.filter(
            id_semielaborado = codigo
        )

########################################################################
class ProductionOrders1Manager(models.Manager):
    
    # Estos 2 metodos son iguales en el resultado
    def reporte_range_duedate(self,fecha1,fecha2):
        return self.filter(
            duedate__range = (fecha1,fecha2)
            )

class ProductionOrders2Manager(models.Manager):
    
    def order_by_parentkey(self,codigo):
        return self.filter(
            parentkey = codigo
        )