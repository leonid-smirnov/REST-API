from django.contrib import admin
from .models import Product
from .forms import ProductForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'currency', 'description', 'url')
    form = ProductForm
