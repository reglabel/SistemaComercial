from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Pessoa(models.Model):
    class Meta:
        abstract = True
    
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome + " " + self.sobrenome

class Cliente(Pessoa):
    ativo = models.BooleanField(default=True)
    
class Vendedor(Pessoa):
    salario = models.FloatField()

class Produto(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    preco = models.FloatField()

    def __str__(self) -> str:
        return self.nome

class Item(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.produto.nome + " , qtd: " + f"{self.quantidade}"


class Carrinho(models.Model):
    codigo = models.CharField(max_length=6, default="-", blank=False)
    itens = models.ManyToManyField(Item)

    def __str__(self) -> str:
        return "Carrinho " + self.codigo
           

class Venda(models.Model):
    codigo = models.CharField(max_length=6, default="-", blank=False)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Venda " + self.codigo
