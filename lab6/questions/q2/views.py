from django.http.response import HttpResponse
from django.shortcuts import render
from . import forms
# Create your views here.
def page1(request):
    return render(request, 'page1.html', { 'bioData': forms.BiodataForms })

def page2(request):
    if request.method == 'POST':
        bd = forms.BiodataForms(request.POST)
        if bd.is_valid():
            request.session['name'] = bd.cleaned_data['name']
            request.session['rollno'] = bd.cleaned_data['rollno']
            request.session['subject'] = bd.cleaned_data['subject']
            return render(request, 'page2.html', { 'name': request.session['name'], 'rollno':  request.session['rollno'], 'subject': request.session['subject'] })

    if request.session.has_key('name'):
        return render(request, 'page2.html', { 'name': request.session['name'], 'rollno':  request.session['rollno'], 'subject': request.session['subject'] })
    else:
        return HttpResponse('Invalid session')