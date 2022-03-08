from django.urls import path
from .views import HomeView,InstrumentiListView,DodajOglas,AzurirajOglas,ObrisiOglas

app_name = 'Instrumenti'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("oglasi/", InstrumentiListView.as_view(), name="oglasi"),
    path("dodaj_oglas/", DodajOglas.as_view(), name="dodaj_oglas"),
    path("update_instrument/<int:pk>",AzurirajOglas.as_view(), name = 'update_instrument'),
    path("delete_instrument/<int:pk>",ObrisiOglas.as_view(), name = 'delete_instrument')
]