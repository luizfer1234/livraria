from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Consumidor)
admin.site.register(Livro)
admin.site.register(Ordem)
admin.site.register(ItemOrdem)
admin.site.register(Enderecoenvio)