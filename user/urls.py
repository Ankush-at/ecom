from django.urls import path
from user import views



urlpatterns = [
	path('',views.home),
	path('addtocart/<int:pk>/',views.addtocart,name='addtocart'),
	path('cart/',views.cart,name='cart'),
	path('delete/<int:pk>/',views.delete,name='delete'),
	path('order/',views.order,name='order'),

]