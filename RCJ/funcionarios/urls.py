from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from RCJ.funcionarios import views as funcionarios_views

app_name = 'funcionarios'
urlpatterns = [
    
    path('lista_funcionarios/', funcionarios_views.list_funcionarios, name = 'lista_funcionario'),
    path('cadastrar_funcionario/', funcionarios_views.create_funcionario, name = 'cadastro_funcionario'),
    path('editar_funcionario/<slug:slug>-<int:pk>', funcionarios_views.edit_funcionario, name = 'editar_funcionario'),
    path('deletar_funcionario/<slug:slug>-<int:pk>', funcionarios_views.delete_funcionario, name = 'deletar_funcionario'),

]
