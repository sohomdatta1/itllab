from django.http.response import HttpResponse
from django.shortcuts import render
from . import forms

cost_table = {
    'HP': {
        'laptop': 8000,
        'tablet': 5000
        },
    'Nokia': {
        'laptop': 9000,
        'tablet': 6000
    },
    'Samsung': {
        'latop': 10000,
        'tablet': 7000
        },
    'Motorola': {
        'laptop': 12000,
        'tablet': 8000
        },
    'Apple': {
        'laptop': 13000,
        'tablet': 9000
        }
}
# Create your views here.
def input(request):
    return render(request, 'a.html', { 'shopping': forms.ShoppingForm })

def output(request):
    if request.method == 'POST':
        shp = forms.ShoppingForm(request.POST)
        if shp.is_valid():
            total_bill = 0
            brand = shp.cleaned_data['brand']
            quantity = shp.cleaned_data['quantity']
            lpt = shp.cleaned_data.get('laptops_or_tablets')
            if 'laptop' in lpt:
                total_bill += cost_table[brand]['laptop'] * int(quantity)
            if 'mobile' in lpt:
                total_bill += cost_table[brand]['tablet'] * int(quantity)
            return render(request, 'b.html', { 'bill': total_bill })

    return HttpResponse('Invalid request')