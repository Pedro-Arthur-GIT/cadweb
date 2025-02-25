import locale
from django import forms
from django.db import models
from decimal import Decimal
import hashlib


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    ordem = models.IntegerField()


    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15,verbose_name="CPF")
    datanasc = models.DateField(verbose_name="Data de Nascimento")


    def __str__(self):
        return self.nome
    
    @property
    def datanascimento(self):
        """Retorna a data de nascimento no formato DD/MM/AAAA"""
        if self.datanasc:
            return self.datanasc.strftime('%d/%m/%Y')
        return None
    
    @property
    def cpf_formatado(self):
        """Retorna o CPF formatado como XXX.XXX.XXX-XX"""
        cpf_numerico = "".join(filter(str.isdigit, self.cpf))  # Remove não numéricos
        return f"{cpf_numerico[:3]}.{cpf_numerico[3:6]}.{cpf_numerico[6:9]}-{cpf_numerico[9:]}" if len(cpf_numerico) == 11 else "CPF inválido"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img_base64 = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    
    @property
    def estoque(self):
        # Tenta buscar o estoque, se não existir, cria um novo com quantidade 0
        estoque_item, flag_created = Estoque.objects.get_or_create(produto=self, defaults={'qtde': 0})
        return estoque_item

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde = models.IntegerField()

    def __str__(self):
         return f'{self.produto.nome} - Quantidade: {self.qtde}'
    
class Pedido(models.Model):


    NOVO = 1
    EM_ANDAMENTO = 2
    CONCLUIDO = 3
    CANCELADO = 4


    STATUS_CHOICES = [
        (NOVO, 'Novo'),
        (EM_ANDAMENTO, 'Em Andamento'),
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado'),
    ]


    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NOVO)


    def __str__(self):
            return f"Pedido {self.id} - Cliente: {self.cliente.nome} - Status: {self.get_status_display()}"
    @property
    def data_pedidof(self):
        """Retorna a data no formato DD/MM/AAAA HH:MM"""
        if self.data_pedido:
            return self.data_pedido.strftime('%d/%m/%Y %H:%M')
        return None
    
    @property
    def total(self):
        """Calcula o total de todos os itens no pedido, formatado como moeda local"""
        total = sum(item.qtde * item.preco for item in self.itempedido_set.all())
        return total
    
    @property
    def qtdeItens(self):
        """Conta a qtde de itens no pedido, """
        return self.itempedido_set.count()  
    
       # lista de todos os pagamentos realiados
    @property
    def pagamentos(self):
        return Pagamento.objects.filter(pedido=self)    
    
    #Calcula o total de todos os pagamentos do pedido
    @property
    def total_pago(self):
        total_pago = sum(pagamento.valor for pagamento in self.pagamentos.all())
        return total_pago    
    
    @property
    def debito(self):
        debito = self.total - self.total_pago
        return debito

    def format_decimal(self, value):
        return value.quantize(Decimal("0.01"))  # Apenas formata, sem arredondar

    @property
    def icms(self):
        return self.format_decimal(self.total * Decimal("0.18"))

    @property
    def ipi(self):
        return self.format_decimal(self.total * Decimal("0.05"))

    @property
    def pis(self):
        return self.format_decimal(self.total * Decimal("0.0165"))

    @property
    def cofins(self):
        return self.format_decimal(self.total * Decimal("0.076"))

    @property
    def impostos(self):
        return self.format_decimal(self.icms + self.ipi + self.pis + self.cofins)
    
    @property
    def valor_final(self):
        return self.format_decimal(self.total + self.impostos)

    @property
    def chave_acesso(self):
        """Gera uma chave de acesso numérica baseada no ID do pedido e na data da nota fiscal"""
        if not self.data_pedido:
            return "00000000000000000000000000000000000000000000"  # Caso não tenha data

        # Concatena ID + data no formato YYYYMMDD
        chave_base = f"{self.id}{self.data_pedido.strftime('%Y%m%d')}"
        
        # Gera um hash numérico
        chave_hash = hashlib.sha256(chave_base.encode()).hexdigest()

        # Converte letras em números (A=0, B=1, ..., F=5) e mantém apenas números
        chave_numerica = ''.join(str(int(char, 16)) for char in chave_hash)[:44]  # Limita a 44 caracteres

        return chave_numerica
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.produto.nome} (Qtd: {self.qtde}) - Preço Unitário: {self.preco}"    

    @property
    def subtotal(self):
        """Calcula o subtotal do item (quantidade * preço unitário)"""
        return self.qtde * self.preco
    
class Pagamento(models.Model):
    DINHEIRO = 1
    CARTAO = 2
    PIX = 3
    OUTRA = 4


    FORMA_CHOICES = [
        (DINHEIRO, 'Dinheiro'),
        (CARTAO, 'Cartão'),
        (PIX, 'Pix'),
        (OUTRA, 'Outra'),
    ]


    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    forma = models.IntegerField(choices=FORMA_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    data_pgto = models.DateTimeField(auto_now_add=True)
    
    @property
    def data_pgtof(self):
        """Retorna a data no formato DD/MM/AAAA HH:MM"""
        if self.data_pgto:
            return self.data_pgto.strftime('%d/%m/%Y %H:%M')
        return None

