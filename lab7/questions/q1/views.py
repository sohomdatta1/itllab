from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def index(request):
    categories = models.Category.objects.all()
    pages = models.Page.objects.all()
    return render(request, 'index.html', { 'pageForm': forms.PageForm, 'categoryForm': forms.CategoryForm, 'categories': categories, 'pages': pages })

def register_cat(request):
    if request.method == 'POST':
        cat = forms.CategoryForm(request.POST)
        if cat.is_valid():
            cat.save(commit=True)
            return HttpResponseRedirect('/q1')
    return HttpResponse('Invalid response')

def register_page(request):
    if request.method == 'POST':
        page = forms.PageForm(request.POST)
        if page.is_valid():
            page.save(commit=True)
            return HttpResponseRedirect('/q1')
    return HttpResponse('Invalid response')
