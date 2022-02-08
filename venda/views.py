from django.shortcuts import render
from .models import *

def venda(request):
    livros = Livro.objects.all()
    context = {'livros':livros}
    return render(request, 'venda/venda.html', context)

def carrinhocompras(request):
    context = {}
    return render(request, 'venda/carrinhocompras.html', context)

def finalizarpedido(request):
    context = {}
    return render(request, 'venda/finalizarpedido.html', context)
