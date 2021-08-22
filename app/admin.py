from django.contrib import admin
from .models import Meal, Order, OrderMeal

# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']

admin.site.register(Meal, MealAdmin)
admin.site.register(Order)
admin.site.register(OrderMeal)