from django import forms
from .models import Instrument,Nalozi

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = '__all__'

        widgets = {
            'marka': forms.TextInput(attrs={'class':'form-control'}),
            'model': forms.TextInput(attrs={'class':'form-control'}),
            'opis': forms.TextInput(attrs={'class':'form-control'}),
            'cena': forms.TextInput(attrs={'class':'form-control'}),
            'kontakt': forms.TextInput(attrs={'class':'form-control'}),
            'mesto': forms.TextInput(attrs={'class':'form-control'})
        }

class LogIn(forms.Form):
    email = forms.CharField(label = 'Email', max_length=30)
    lozinka = forms.CharField(label = 'Lozinka', max_length=30, widget=forms.TextInput(attrs={'type': 'password'}))


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Nalozi
        fields = '__all__'

        widgets = {
            'ime': forms.TextInput(attrs={'class':'form-control'}),
            'prezime': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'brtel': forms.TextInput(attrs={'class':'form-control'}),
            'lozinka': forms.TextInput(attrs={'class':'form-control', 'type':'password'})
        }