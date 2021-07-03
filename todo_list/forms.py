from django import forms
from .models import list, Work_Volume

class Listform (forms.ModelForm):
    class Meta:
        model = list
        fields= ["item", "completed"]


class WorkVolumeform (forms.ModelForm):
    class Meta:
        model = Work_Volume
        fields= ["Tx_Name", "Is_Active"]