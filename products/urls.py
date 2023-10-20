from django.urls import path
from . import views

urlpatterns=[
    path('products/view_products',views.view_products,name="view_products")
]