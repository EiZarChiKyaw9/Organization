from django import forms
from .models import list

class Listform (forms.ModelForm):
    class Meta:
        model = list
        fields= ["item", "completed"]