from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .models import Instrument
from .forms import InstrumentForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Instrumenti/home.html'

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