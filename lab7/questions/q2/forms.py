
from django import forms
from . import models
class WorksForm(forms.ModelForm):
    class Meta:
        model = models.Works
        exclude = ()

class LivesForm(forms.ModelForm):
    class Meta:
        model = models.Lives
        exclude = ()

class Company(forms.Form):
    company_name = forms.CharField()