from django import forms
from .models import Product

class ProductForm(forms.ModelForm):  #  Класс форм текстовых полей для админки

    # def clean_url(self):
    #     url = self.cleaned_data['url']

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'url'
        )
        widgets = {
            'title': forms.TextInput,
        }
