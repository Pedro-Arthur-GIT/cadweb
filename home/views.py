from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import pdfkit
from django.template.loader import render_to_string






@login_required
def index(request):
    return render(request,'index.html')

@login_required
def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/lista.html', contexto)

@login_required
def form_categoria(request):
    if request.method == 'POST':
       form = CategoriaForm(request.POST) # instancia o modelo com os dados do form
       if form.is_valid():# faz a validação do formulário
            form.save() # salva a instancia do modelo no banco de dados
            messages.success(request, "Operação realizada com sucesso")
            return redirect('categoria') # redireciona para a listagem
    else:# método é get, novo registro
        form = CategoriaForm() # formulário vazio
    contexto = {
        'form':form,
    }
    return render(request, 'categoria/formulario.html', contexto)

@login_required
def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('categoria')  # Redireciona para a listagem

    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save() # save retorna o objeto salvo
            messages.success(request, "Operação realizada com sucesso")
            return redirect('categoria') # redireciona para a listagem

    else:
         form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/editar_categoria.html', {'form': form, 'categoria': categoria})

@login_required
def detalhes_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
          # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('categoria')  # Redireciona para a listagem
    return render(request, 'categoria/detalhes_categoria.html', {'categoria': categoria})

@login_required
def excluir_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id) 
        produto.delete()
        messages.success(request, "Operação realizada com sucesso")
        return redirect('categoria')
    except Categoria.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
    return redirect('categoria')  # Redireciona para a listagem


@login_required
def cliente(request):
    contexto = {
        'lista': Cliente.objects.all().order_by('id'),
    }
    return render(request, 'cliente/lista_cliente.html', contexto)

@login_required
def formulario_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # instancia o modelo com os dados do form
        if form.is_valid():  # faz a validação do formulário
            form.save()  # salva a instância do modelo no banco de dados
            messages.success(request, "Operação realizada com sucesso")
            return redirect('cliente')  # redireciona para a listagem
    else:  # método é get, novo registro
        form = ClienteForm()  # formulário vazio
    contexto = {
        'form': form,
    }
    return render(request, 'cliente/formulario_cliente.html', contexto)

@login_required
def editar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('cliente')  # Redireciona para a listagem

    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()  # save retorna o objeto salvo
            messages.success(request, "Operação realizada com sucesso")
            return redirect('cliente')  # redireciona para a listagem

    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/editar_cliente.html', {'form': form, 'cliente': cliente})

@login_required
def detalhes_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('cliente')  # Redireciona para a listagem
    return render(request, 'cliente/detalhes_cliente.html', {'cliente': cliente})

@login_required
def excluir_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id) 
        produto.delete()
        messages.success(request, "Operação realizada com sucesso")
        return redirect('cliente')
    except Cliente.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
    return redirect('cliente')  # Redireciona para a listagem




@login_required
def produto(request):
    contexto = {
        'lista': Produto.objects.all().order_by('id'),
    }
    return render(request, 'produto/lista_produto.html', contexto)

@login_required
def form_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)  # instancia o modelo com os dados do form
        if form.is_valid():  # faz a validação do formulário
            form.save()  # salva a instância do modelo no banco de dados
            messages.success(request, "Operação realizada com sucesso")
            return redirect('produto')  # redireciona para a listagem
    else:  # método é get, novo registro
        form = ProdutoForm()  # formulário vazio
    contexto = {
        'form': form,
    }
    return render(request, 'produto/form_produto.html', contexto)

@login_required
def editar_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('produto')  # Redireciona para a listagem

    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save()  # save retorna o objeto salvo
            messages.success(request, "Operação realizada com sucesso")
            return redirect('produto')  # redireciona para a listagem

    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto/editar_produto.html', {'form': form, 'produto': produto})

@login_required
def detalhes_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Cliente.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('produto')  # Redireciona para a listagem
    return render(request, 'produto/detalhes_produto.html', {'produto': produto})

@login_required
def remover_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id) 
        produto.delete()
        messages.success(request, "Operação realizada com sucesso")
        return redirect('produto')
    except Produto.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
    return redirect('produto')  # Redireciona para a listagem
   
@login_required   
def ajustar_estoque(request, id):
    produto = Produto.objects.get(pk=id)
    estoque = produto.estoque # pega o objeto estoque relacionado ao produto

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance = estoque)
        if form.is_valid():
            estoque = form.save()
            lista = []
            lista.append(estoque.produto) 
            return render(request, 'produto/lista_produto.html', {'lista': lista})
    else:
         form = EstoqueForm(instance = estoque)
    return render(request, 'produto/estoque.html', {'form': form,})

@login_required
def teste1(request):
    return render(request, 'testes/teste1.html')

@login_required
def teste2(request):
    return render(request, 'testes/teste2.html')

@login_required
def teste3(request):
    return render(request, 'testes/teste3.html')

@login_required
def buscar_dados(request, app_modelo):
    termo = request.GET.get('q', '') # pega o termo digitado
    try:
        # Divida o app e o modelo
        app, modelo = app_modelo.split('.')
        modelo = apps.get_model(app, modelo)
    except LookupError:
        return JsonResponse({'error': 'Modelo não encontrado'}, status=404)
    
    # Verifica se o modelo possui os campos 'nome' e 'id'
    if not hasattr(modelo, 'nome') or not hasattr(modelo, 'id'):
        return JsonResponse({'error': 'Modelo deve ter campos "id" e "nome"'}, status=400)
    
    resultados = modelo.objects.filter(nome__icontains=termo)
    dados = [{'id': obj.id, 'nome': obj.nome} for obj in resultados]
    return JsonResponse(dados, safe=False)

@login_required
def pedido(request):
    lista = Pedido.objects.all().order_by('-id') #Obtem todos os registros
    return render(request, 'pedido/lista.html', {'lista' : lista})

@login_required
def novo_pedido(request,id):
    if request.method == 'GET':
        try:
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            # Caso o registro não seja encontrado, exibe a mensagem de erro
            messages.error(request, 'Registro não encontrado')
            return redirect('cliente')  # Redireciona para a listagem
        # cria um novo pedido com o cliente selecionado
        pedido = Pedido(cliente=cliente)
        form = PedidoForm(instance=pedido)# cria um formulario com o novo pedido
        return render(request, 'pedido/form_pedido.html',{'form': form,})
    else: # se for metodo post, salva o pedido.
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('detalhes_pedido', id=pedido.id)

@login_required
def remover_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id) 
        pedido.delete()
        messages.success(request, "Operação realizada com sucesso")
        return redirect('pedido')
    except Produto.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
    return redirect('pedido')  # Redireciona para a listagem

@login_required
def detalhes_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')
    
    if request.method == 'GET':
        itemPedido = ItemPedido(pedido=pedido)
        form = ItemPedidoForm(instance=itemPedido)
    else:  # method POST
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)  # Não salva ainda, para modificações
            item_pedido.preco = item_pedido.produto.preco  # Define o preço do produto
            
            # Verifica se há estoque suficiente
            estoque = item_pedido.produto.estoque
            if item_pedido.qtde > estoque.qtde:
                messages.error(request, 'Estoque insuficiente para este produto!')
            else:
                # Atualiza o estoque do produto
                estoque.qtde -= item_pedido.qtde
                estoque.save()  # Salva a nova quantidade no banco
                item_pedido.save()  # Agora salva o item no pedido
                messages.success(request, 'Produto adicionado ao pedido com sucesso!')
                return redirect('detalhes_pedido', id=pedido.id)
        else:
            messages.error(request, 'Erro ao adicionar produto')
    
    contexto = {
        'pedido': pedido,
        'form': form,
    }
    return render(request, 'pedido/detalhes_pedido.html', contexto)

@login_required
def editar_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)
    
    pedido = item_pedido.pedido  
    quantidade_anterior = item_pedido.qtde  # A quantidade que já foi reservada anteriormente

    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item_pedido)
        if form.is_valid():
            item_pedido = form.save(commit=False)  # Não salva ainda, para modificações
            produto = item_pedido.produto
            nova_quantidade = item_pedido.qtde

  

            # Devolvendo a quantidade anterior ao estoque
            estoque = item_pedido.produto.estoque  # Obtém o estoque do produto
            estoque.qtde += quantidade_anterior  # Devolve a quantidade do item ao estoque
            estoque.save() 



            # Verificando se o estoque é suficiente
            if nova_quantidade > produto.estoque.qtde:
                print(f"Erro: estoque insuficiente para {produto.nome} (estoque: {produto.estoque.qtde}, solicitado: {nova_quantidade})")
                messages.error(request, 'Quantidade em estoque insuficiente para o produto.')
            else:
                # Atualizando o estoque com a nova quantidade

                estoque.qtde -= nova_quantidade
                estoque.save()
  

                item_pedido.save()  # Salva o item atualizado
                messages.success(request, 'Operação realizada com sucesso')
                return redirect('detalhes_pedido', id=pedido.id)
        else:
            messages.error(request, 'Erro ao atualizar o item do pedido.')
    else:
        form = ItemPedidoForm(instance=item_pedido)
    
    contexto = {
        'pedido': pedido,
        'form': form,
        'item_pedido': item_pedido,
    }
    return render(request, 'pedido/detalhes_pedido.html', contexto)

@login_required
def remover_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)
    
    pedido_id = item_pedido.pedido.id  # Armazena o ID do pedido antes de remover o item
    estoque = item_pedido.produto.estoque  # Obtém o estoque do produto
    estoque.qtde += item_pedido.qtde  # Devolve a quantidade do item ao estoque
    estoque.save()  # Salva as alterações no estoque
    # Remove o item do pedido
    item_pedido.delete()
    messages.success(request, 'Operação realizada com Sucesso')


    # Redireciona de volta para a página de detalhes do pedido
    return redirect('detalhes_pedido', id=pedido_id)

@login_required
def form_pagamento(request,id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  # Redireciona para a listagem    
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operação realizada com Sucesso')
        else:
            messages.error(request, 'Corrija os erros do formulário.')
    # prepara o formulário para um novo pagamento
    pagamento = Pagamento(pedido=pedido)
    form = PagamentoForm(instance=pagamento)
    contexto = {
        'pedido': pedido,
        'form': form,
    }    
    return render(request, 'pedido/pagamento.html',contexto)

@login_required
def remover_pagamento(request, id):
    try:
        pagamento = Pagamento.objects.get(pk=id) 
        pedido = pagamento.pedido
        pagamento.delete()
        messages.success(request, "Operação realizada com sucesso")
        return redirect('form_pagamento', id=pedido.id)
    except Pagamento.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
    return redirect('form_pagamento', id=pedido.id)

@login_required
def editar_pagamento(request, id):
    try:
        pagamento = Pagamento.objects.get(pk=id)
        pedido = pagamento.pedido
    except Pagamento.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('form_pagamento', id=pedido.id)  # Redireciona para a listagem

    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            pagamento = form.save()  # save retorna o objeto salvo
            messages.success(request, "Operação realizada com sucesso")
            return redirect('form_pagamento', id=pedido.id)  # redireciona para a listagem

    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'pedido/pagamento.html', {'form': form, 'pedido': pedido, 'id':id})

@login_required
def nota_fiscal(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido', id=id)
    return render(request, 'pedido/nota_fiscal.html', {'pedido': pedido})

def pdf(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    html_string = render_to_string('pedido/nota_fiscal.html', {'pedido': pedido})

    # Configuração do pdfkit
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')  # Ajuste o caminho conforme necessário

    # Gerar PDF
    pdf_file = pdfkit.from_string(html_string, False, configuration=config)

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pedido_{pedido.id}.pdf"'
    return response







