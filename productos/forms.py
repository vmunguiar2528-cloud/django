from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'categoria', 'proveedor', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'erp-input'}),
            'precio': forms.NumberInput(attrs={'class': 'erp-input', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'erp-input'}),
            'categoria': forms.Select(attrs={'class': 'erp-input'}),
            'proveedor': forms.Select(attrs={'class': 'erp-input'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
