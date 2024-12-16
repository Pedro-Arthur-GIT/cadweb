from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/lista', views.categoria, name="categoria"),
    path('categoria/formulario', views.form_categoria, name="form_categoria"),
    path('categoria/detalhes_categoria/<int:id>/', views.detalhes_categoria, name = "detalhes_categoria"),
    path('categoria/editar_categoria/<int:id>/', views.editar_categoria, name = "editar_categoria"),
    path('categoria/excluir_categoria/<int:id>/', views.excluir_categoria, name = "excluir_categoria"),
]