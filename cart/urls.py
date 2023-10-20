from django.urls import path
from . import views

urlpatterns = [
    path('cart/viewCart',views.viewCart,name="viewCart")

]