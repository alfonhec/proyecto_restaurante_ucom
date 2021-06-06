from django.urls import path, include
from catalogos import views


urlpatterns = [
    path('', views.index, name="index"),
    path('clientes/', views.cliente, name="cliente"),
    path('nuevo/', views.formCliente, name="nuevoCliente"),
    path('pedidos/', views.pedidos, name="pedidos")
]