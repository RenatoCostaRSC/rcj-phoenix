from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from RCJ.core import views as core_views

app_name = 'core'
urlpatterns = [
    
    #path('lista_funcionarios/', funcionarios_views.list_funcionarios, name = 'lista_funcionario'),
    path('implantar_ficha/', core_views.implanta_ficha_cliente, name = 'implantar_ficha'),
    path('cadastrar_produto/', core_views.create_produto, name = 'cadastrar_produto'),
    path('fila_clientes/', core_views.fila_clientes, name = 'fila_clientes'),
    path('tratar_cliente/<slug:slug>-<int:pk>', core_views.tratar_clientes, name = 'tratar_cliente'),
    #path('deletar_funcionario/<int:pk>-<slug:slug>', funcionarios_views.delete_funcionario, name = 'deletar_funcionario'),

]