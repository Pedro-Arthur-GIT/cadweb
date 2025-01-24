from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse
from django.apps import apps




def index(request):
    return render(request,'index.html')

def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/lista.html', contexto)

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

def detalhes_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
          # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('categoria')  # Redireciona para a listagem
    return render(request, 'categoria/detalhes_categoria.html', {'categoria': categoria})

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



def cliente(request):
    contexto = {
        'lista': Cliente.objects.all().order_by('id'),
    }
    return render(request, 'cliente/lista_cliente.html', contexto)


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

def detalhes_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('cliente')  # Redireciona para a listagem
    return render(request, 'cliente/detalhes_cliente.html', {'cliente': cliente})

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





def produto(request):
    contexto = {
        'lista': Produto.objects.all().order_by('id'),
    }
    return render(request, 'produto/lista_produto.html', contexto)

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

def editar_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Cliente.DoesNotExist:
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

def detalhes_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Cliente.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('produto')  # Redireciona para a listagem
    return render(request, 'produto/detalhes_produto.html', {'produto': produto})


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

def teste1(request):
    return render(request, 'testes/teste1.html')

def teste2(request):
    return render(request, 'testes/teste2.html')

def teste3(request):
    return render(request, 'testes/teste3.html')

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

def pedido(request):
    lista = Pedido.objects.all().order_by('-id') #Obtem todos os registros
    return render(request, 'pedido/lista.html', {'lista' : lista})

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
            return redirect('pedido')

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

def detalhes_pedido(request, id):
    try:
        pedido= Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  # Redireciona para a listagem
    return render(request, 'pedido/detalhes_pedido.html', {'pedido': pedido})