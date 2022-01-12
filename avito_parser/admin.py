from django.contrib import admin
from .models import Product
from .forms import ProductForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('published_date', 'title', 'room_number', 'floor', 'price', 'description', 'url')
    fields = ('published_date', 'title',  'room_number', 'price', 'floor', 'description', 'url')
    form = ProductForm
