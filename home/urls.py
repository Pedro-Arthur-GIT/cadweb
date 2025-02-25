from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/lista', views.categoria, name="categoria"),
    path('categoria/formulario', views.form_categoria, name="form_categoria"),
    path('categoria/detalhes_categoria/<int:id>/', views.detalhes_categoria, name = "detalhes_categoria"),
    path('categoria/editar_categoria/<int:id>/', views.editar_categoria, name = "editar_categoria"),
    path('categoria/excluir_categoria/<int:id>/', views.excluir_categoria, name = "excluir_categoria"),

    path('cliente/lista_cliente', views.cliente, name="cliente"),
    path('cliente/formulario_cliente', views.formulario_cliente, name="formulario_cliente"),
    path('cliente/detalhes_cliente/<int:id>/', views.detalhes_cliente, name="detalhes_cliente"),
    path('cliente/editar_cliente/<int:id>/', views.editar_cliente, name="editar_cliente"),
    path('cliente/excluir_cliente/<int:id>/', views.excluir_cliente, name="excluir_cliente"),

    path('produto/', views.produto, name='produto'),
    path('form_produto/', views.form_produto, name='form_produto'),
    path('detalhes_produto/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('remover_produto/<int:id>/', views.remover_produto, name='remover_produto'),

    path('ajustar_estoque/<int:id>/', views.ajustar_estoque, name='ajustar_estoque'),

    path('teste1/', views.teste1, name='teste1'),
    path('teste2/', views.teste2, name='teste2'),
    path('teste3/', views.teste3, name='teste3'),

    path('buscar_dados/<str:app_modelo>/', views.buscar_dados, name='buscar_dados'),

    path('pedido/lista/', views.pedido, name='pedido'),
    path('pedido/novo_pedido/<int:id>/', views.novo_pedido, name='novo_pedido'),
    path('pedido/remover_pedido/<int:id>/', views.remover_pedido, name='remover_pedido'),
    path('pedido/detalhes_pedido/<int:id>/', views.detalhes_pedido, name='detalhes_pedido'),
    
    path('pedido/editar_item_pedido/<int:id>/', views.editar_item_pedido, name='editar_item_pedido'),
    path('pedido/remover_item_pedido/<int:id>/', views.remover_item_pedido, name='remover_item_pedido'),
    path('pedido/form_pagamento/<int:id>/', views.form_pagamento, name='form_pagamento'),
    path('pedido/editar_pagamento/<int:id>/', views.editar_pagamento, name='editar_pagamento'),
    path('pedido/remover_pagamento/<int:id>/', views.remover_pagamento, name='remover_pagamento'),

    path('pedido/nota_fiscal/<int:id>/', views.nota_fiscal, name='nota_fiscal'),
    path('pedido/pdf/<int:id>/', views.pdf, name='pdf'),
]