from django import forms
from .models import Product

class ProductForm(forms.ModelForm):  #  Класс форм текстовых полей для админки

    # def clean_url(self):
    #     url = self.cleaned_data['url']

    class Meta:
        model = Product
        fields = (
            'title',
            'room_number',
            'floor',
            'floors',
            'published_date',
            'price',
            'url',
        )
        widgets = {
            'title': forms.TextInput,
            'room_number': forms.TextInput,
            'published_date': forms.TextInput,
            'floor': forms.TextInput,
            'floors': forms.TextInput,
            'price': forms.TextInput,
            'url': forms.TextInput,

        }
