from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def index(request):
    lives = models.Lives.objects.all()
    works = models.Works.objects.all()
    return render(request, 'index1.html', { 'workform': forms.WorksForm, 'livesform': forms.LivesForm, 'lives': lives, 'works': works })

def register_work(request):
    if request.method == 'POST':
        wk = forms.WorksForm(request.POST)
        if wk.is_valid():
            wk.save(commit=True)
            return HttpResponseRedirect('/q2/')
    return HttpResponse('Invalid request')

def register_live(request):
    if request.method == 'POST':
        lv = forms.LivesForm(request.POST)
        if lv.is_valid():
            lv.save(commit=True)
            return HttpResponseRedirect('/q2/')
    return HttpResponse('Invalid request')

def get_for_company(request):
    companies = []
    if request.method == "POST":
        cm = forms.Company(request.POST)
        if cm.is_valid():
            companies = models.Works.objects.filter(company_name=cm.cleaned_data['company_name']).select_related()
    return render(request, 'gfc.html', {'companyform': forms.Company, 'companies': companies})