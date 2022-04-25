
from django import forms
from django.forms.fields import CharField, EmailField
from django.forms.widgets import EmailInput, PasswordInput, TextInput

class LoginForm(forms.Form):
    username = CharField(widget=TextInput, required=True)
    password = CharField(widget=PasswordInput)
    email = CharField(widget=EmailInput)
    contact = CharField(widget=TextInput)
