from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .models import Instrument

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Instrumenti/home.html'

class InstrumentiListView(ListView):
    model = Instrument
    queryset = Instrument.objects.order_by('marka')
    context_object_name = "Instrumenti_list"

class DodajOglas(CreateView):
    model = Instrument
    fields = "__all__"
    success_url = reverse_lazy('Instrumenti:oglasi')

class AzurirajOglas(UpdateView):
    model = Instrument
    fields = "__all__"
    success_url = reverse_lazy('Instrumenti:oglasi')

class ObrisiOglas(DeleteView):
    model = Instrument
    success_url = reverse_lazy('Instrumenti:oglasi')