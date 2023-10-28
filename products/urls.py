from django.urls import path
from . import views

urlpatterns=[
    path('view_products',views.view_products,name="view_products"),
    path('all_products',views.all_products, name="all_products")
]