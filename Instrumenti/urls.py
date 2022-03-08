from django.urls import path
from .views import HomeView,InstrumentiListView,DodajOglas,InstrumentUpdate

app_name = 'Instrumenti'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("oglasi/", InstrumentiListView.as_view(), name="oglasi"),
    path("dodaj_oglas/", DodajOglas.as_view(), name="dodaj_oglas"),
    path("update_instrument/<int:pk>",InstrumentUpdate.as_view(), name = 'update_instrument')
]