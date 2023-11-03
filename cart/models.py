from django.db import models

# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=60) 
    price = models.IntegerField(default=0) 
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    description = models.CharField( 
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/') 

class Order(models.Model):
    product = models.ForeignKey(Products, 
                                on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer, 
                                 on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1) 
    price = models.IntegerField() 
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=False) 