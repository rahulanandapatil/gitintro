from django.contrib import admin
from .models import Product,Contact,Burger,Price,Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Burger)
admin.site.register(Order)
admin.site.register(Price)
