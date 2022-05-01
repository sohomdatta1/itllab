from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from . import models
# Create your views here.
def index(request):
    if request.method == 'POST':
        dt = forms.PollForm(request.POST)
        if dt.is_valid():
            chc = models.PollModel.objects.get(choice_text=dt.cleaned_data['choice'])
            chc.votes += 1
            chc.save()
            return HttpResponseRedirect('/myapp/1/results')
        else:
            print(dt.errors)
    return render(request, 'index.html', { 'question': models.QuestionModel.objects.all()[0] })

def results(request):
    poll_data = models.PollModel.objects.all()
    return render(request, 'index1.html', { 'poll_data': poll_data })