from django.db import models

# Create your models here.
class Instrument(models.Model):
    marka = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    opis = models.CharField(max_length=30)
    cena = models.CharField(max_length=30)
    kontakt = models.CharField(max_length=30)
    mesto = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.marka} {self.model}"