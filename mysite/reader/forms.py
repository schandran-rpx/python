# reader/forms.py

from django import forms
from .models import KTRFile

class KTRFileForm(forms.ModelForm):
    class Meta:
        model = KTRFile
        fields = ['file']
