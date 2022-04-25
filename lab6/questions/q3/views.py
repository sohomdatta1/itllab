from django.http.response import HttpResponse
from django.shortcuts import render
from . import forms
# Create your views here.
def login(request):
    return render(request, 'login.html', { 'login': forms.LoginForm })

def home(request):
    if request.method == 'POST':
        lg = forms.LoginForm(request.POST)
        if lg.is_valid():
            return render(request, 'home.html', { 'username': lg.cleaned_data['username'], 'email': lg.cleaned_data['email'], 'contact': lg.cleaned_data['contact'] })
    return HttpResponse('Invalid request')