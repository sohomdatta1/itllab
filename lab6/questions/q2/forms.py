
from django import forms

class BiodataForms(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    rollno = forms.IntegerField(widget=forms.NumberInput)
    subject = forms.ChoiceField(widget=forms.Select, choices=(('Physics','Physics'), ('Chemistry','Chemistry'), ('Math','Math'), ('Biology','Biology')))