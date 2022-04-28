
from django import forms
from . import models

class PageForm(forms.ModelForm):
    class Meta:
        model = models.Page
        exclude = ()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        exclude = ()