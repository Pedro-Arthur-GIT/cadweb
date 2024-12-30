from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/lista', views.categoria, name="categoria"),
    path('categoria/formulario', views.form_categoria, name="form_categoria"),
    path('categoria/detalhes_categoria/<int:id>/', views.detalhes_categoria, name = "detalhes_categoria"),
    path('categoria/editar_categoria/<int:id>/', views.editar_categoria, name = "editar_categoria"),
    path('categoria/excluir_categoria/<int:id>/', views.excluir_categoria, name = "excluir_categoria"),
    path('categoria/tabela', views.tabela_categoria, name="tabela_categoria"),

    path('cliente/lista_cliente', views.cliente, name="cliente"),
    path('cliente/formulario_cliente', views.formulario_cliente, name="formulario_cliente"),
    path('cliente/detalhes_cliente/<int:id>/', views.detalhes_cliente, name="detalhes_cliente"),
    path('cliente/editar_cliente/<int:id>/', views.editar_cliente, name="editar_cliente"),
    path('cliente/excluir_cliente/<int:id>/', views.excluir_cliente, name="excluir_cliente"),
    path('cliente/tabela_cliente', views.tabela_cliente, name="tabela_cliente"),

]