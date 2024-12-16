from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/formulario', views.form_categoria, name="form_categoria"),
]