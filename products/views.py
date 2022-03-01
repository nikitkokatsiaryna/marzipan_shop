from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm
import redis


def main_page(request):
    return render(request, 'main.html')


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)


def create_product(request):
    form = ProductForm

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid:
            product = form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'products/project_form.html', context)

