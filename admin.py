from django.contrib import admin
from .models import Category, Dish, Order, OrderItem, Review

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)


