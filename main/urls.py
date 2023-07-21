from django.urls import path
from . import views

urlpatterns = [
    path ('', views.sorvete_pedido, name = 'pedido'),
    path ('lista', views.pedidos, name = 'lista_pedidos'), #A palavra lista é o que chamamos no URLs
]

