from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .models import Instrument,Nalozi
from .forms import InstrumentForm,LogIn,RegisterForm

# Create your views here.
def HomeView(request):
    if request.method == 'POST':
        form = LogIn(request.POST)

        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['lozinka'])
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