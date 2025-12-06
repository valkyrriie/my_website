from django import forms
from .models import Deals


class DealForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = ['time', 'deal']