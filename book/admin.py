from django.contrib import admin

from book.models import Category,Products

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)