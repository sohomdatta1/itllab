from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index1.html', {})

def index2(request):
    return render(request, 'login.html', {})