from django.urls import path
from .views import HomeView,InstrumentiListView,DodajOglas,AzurirajOglas,ObrisiOglas,RegistrujKorisnika

app_name = 'Instrumenti'

urlpatterns = [
    path("", HomeView, name="home"),
    path("oglasi/", InstrumentiListView.as_view(), name="oglasi"),
    path("dodaj_oglas/", DodajOglas.as_view(), name="dodaj_oglas"),
    path("update_instrument/<int:pk>",AzurirajOglas.as_view(), name = 'update_instrument'),
    path("delete_instrument/<int:pk>",ObrisiOglas.as_view(), name = 'delete_instrument'),
    path("registruj_korisnika",RegistrujKorisnika.as_view(), name = 'register_user')
]