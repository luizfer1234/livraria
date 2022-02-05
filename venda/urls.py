from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.venda, name="venda"),
	path('carrinhocompras/', views.carrinhocompras, name="carrinhocompras"),
	path('finalizarpedido/', views.finalizarpedido, name="finalizarpedido"),

]