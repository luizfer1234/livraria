from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('carrinhocompras/', views.cart, name="cart"),
	path('finalizarpedido/', views.checkout, name="checkout"),

]