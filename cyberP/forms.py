from django import forms
from cyberP.models import Cyberparlement


class CyberparlementChangeForm(forms.ModelForm):
    class Meta:
        model = Cyberparlement
        exclude = ['cyberparlementparent', 'slug']


class CyberparlementCreationForm(forms.ModelForm):
    class Meta:
        model = Cyberparlement
        exclude = ['cyberparlementparent', 'slug']
