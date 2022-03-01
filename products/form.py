from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    # product_image = forms.ImageField(widget=forms.ImageField(attrs={'type': 'file'}))

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['description'].widget.attrs.update({'rows': 2})
