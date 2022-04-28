from django.shortcuts import render
from . import forms
from . import models
# Create your views here.

def input(request):
    if request.method == 'POST':
        pf = forms.ProductForm(request.POST)
        if pf.is_valid():
            pf.save(commit=True)
    return render(request, 'index2.html', { 'productform': forms.ProductForm })

def output(request):
    products = models.Product.objects.all()
    return render(request, 'output3.html', { 'products': products })
