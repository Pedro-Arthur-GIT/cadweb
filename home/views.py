from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from .forms import *




def index(request):
    return render(request,'index.html')

def categoria(request):
    contexto = {
        'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/lista.html', contexto)

def tabela_categoria(request):
    contexto = {
       'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/tabela.html', contexto)


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
    except Categoria.DoesNotExist:
          # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('categoria')  # Redireciona para a listagem
    if request.method == 'POST':
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        messages.success(request, "Operação realizada com sucesso")
        return redirect('categoria')
    else:
        categoria = Categoria.objects.get(pk=id)
    return render(request, 'categoria/excluir_categoria.html', {'categoria': categoria})

def cliente(request):
    contexto = {
        'lista': Cliente.objects.all().order_by('id'),
    }
    return render(request, 'cliente/lista_cliente.html', contexto)

def tabela_cliente(request):
    contexto = {
        'lista': Cliente.objects.all().order_by('id'),
    }
    return render(request, 'cliente/tabela_cliente.html', contexto)

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
    except Cliente.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('cliente')  # Redireciona para a listagem
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        messages.success(request, "Operação realizada com sucesso")
        return redirect('cliente')
    else:
        cliente = Cliente.objects.get(pk=id)
    return render(request, 'cliente/excluir_cliente.html', {'cliente': cliente})
