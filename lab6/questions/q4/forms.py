
from django import forms
from django.forms.fields import BooleanField, ChoiceField, IntegerField
from django.forms.widgets import CheckboxInput, NumberInput

class ShoppingForm(forms.Form):
    brand = forms.ChoiceField(widget=forms.RadioSelect, choices=(('HP','HP'),('Nokia', 'Nokia'),('Motorola', 'Motorola'),('Apple', 'Apple')))
    laptops_or_tablets = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=(('laptop', 'latop'),('mobile', 'mobile')))
    quantity = forms.IntegerField(widget=forms.NumberInput)
