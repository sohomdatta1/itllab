
from django import forms

class PollForm(forms.Form):
    choice = forms.ChoiceField(choices=(('EASY','EASY'), ('DIFFICULT', 'DIFFICULT')))
