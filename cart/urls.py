from django.urls import path
from . import views

urlpatterns = [
    path('view_cart',views.view_cart,name="view_cart"),
    path('checkout',views.checkout, name="checkout"),

]