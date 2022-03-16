import pandas as pd
from io import StringIO

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .models import Instrument,Nalozi
from .forms import InstrumentForm,LogIn,RegisterForm,ExcelLoad

# Create your views here.
def HomeView(request):
    if request.method == 'POST':
        form = LogIn(request.POST)

        if form.is_valid():
            try:
                Nalozi.objects.get(email = form.cleaned_data['email'], lozinka = form.cleaned_data['lozinka'])
                return redirect('oglasi/')

            except:
                form = LogIn()

    else:
        form = LogIn()

    return render(request, 'Instrumenti/home.html', context={'form':form})

class InstrumentiListView(ListView):
    model = Instrument
    queryset = Instrument.objects.order_by('marka')
    context_object_name = "Instrumenti_list"

class DodajOglas(CreateView):
    model = Instrument
    form_class = InstrumentForm
    # fields = "__all__"
    template_name = 'Instrumenti/instrument_form.html'
    success_url = reverse_lazy('Instrumenti:oglasi')

class AzurirajOglas(UpdateView):
    model = Instrument
    form_class = InstrumentForm
    # fields = "__all__"
    template_name = 'Instrumenti/instrument_form.html'
    success_url = reverse_lazy('Instrumenti:oglasi')

class ObrisiOglas(DeleteView):
    model = Instrument
    success_url = reverse_lazy('Instrumenti:oglasi')

class RegistrujKorisnika(CreateView):
    model = Nalozi
    form_class = RegisterForm
    template_name = 'Instrumenti/nalozi_form.html'
    success_url = reverse_lazy('Instrumenti:home')

def ExcelView(request):
    df = pd.DataFrame()
    df = df.to_html()
    if request.method == 'POST':
        uploaded_file = request.FILES['document'].read()
        s=str(uploaded_file,'utf-8')
        data = StringIO(s) 
        df=pd.read_csv(data)
        df = df.to_html()

        return HttpResponse(df)

    return render(request, 'Instrumenti/excel.html')