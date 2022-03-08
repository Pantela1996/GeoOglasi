from django import forms
from .models import Instrument

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = '__all__'

        widgets = {
            'marka': forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class':'form-control'}),
            'opis': forms.TextInput(attrs={'class':'form-control'}),
            'cena': forms.TextInput(attrs={'class':'form-control'})
        }