from django.db import models
from Commune.models import Commune


class Regisseur(models.Model):
    nom_complet = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    telephone = models.CharField(max_length=8, blank=False)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom_complet}"
