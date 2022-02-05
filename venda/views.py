from django.shortcuts import render

def venda(request):
    context = {}
    return render(request, 'venda/venda.html', context)

def carrinhocompras(request):
    context = {}
    return render(request, 'venda/carrinhocompras.html', context)

def finalizarpedido(request):
    context = {}
    return render(request, 'venda/finalizarpedido.html', context)
