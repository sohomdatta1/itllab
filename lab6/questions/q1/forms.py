
from django import forms

class CarForm(forms.Form):
    manufacturer = forms.ChoiceField(widget=forms.Select,choices=(('Hyundai','Hyundai'), ("Maruti","Maruti"), ('Tata', 'Tata')))
    model_name = forms.CharField(widget=forms.TextInput)
