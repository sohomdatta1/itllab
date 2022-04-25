from django.shortcuts import redirect, render
from . import forms
# Create your views here.
def input(request):
    return render(request, 'index.html', { 'carForm': forms.CarForm })

def output(request):
    if request.method == 'POST':
        cars = forms.CarForm(request.POST)
        if cars.is_valid():
            return render(request, 'output.html', { 'manufacturer': cars.cleaned_data['manufacturer'], 'model_name': cars.cleaned_data['model_name'] })
        else:
            return render(request, 'output.html', {})
    else:
        return redirect('/input')