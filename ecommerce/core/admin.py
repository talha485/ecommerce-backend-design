from django.contrib import admin
from .models import Product, Category  # add Category here

admin.site.register(Product)
admin.site.register(Category)  # register Category
from .models import CartItem

admin.site.register(CartItem)
