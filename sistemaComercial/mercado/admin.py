from django.contrib import admin
from .models import Cliente, Vendedor, Produto, Carrinho, Venda, Item

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(Venda)
admin.site.register(Item)
