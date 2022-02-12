from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('carrinhocompras/', views.cart, name="cart"),
	path('finalizarpedido/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name='process_order'),
	path('accounts/login/',views.MyLoginView.as_view(), name='login')
	

]