from django.contrib import admin
from .models import TipoProducto, Ciudad, UnidadMedida,Cliente,Producto,MarcaProducto
# Register your models here 2.

admin.site.register(TipoProducto),
admin.site.register(UnidadMedida),
admin.site.register(Ciudad),
admin.site.register(Cliente),
admin.site.register(Producto),
admin.site.register(MarcaProducto)
