from datetime import date
from django.db import models
from Regisseur.models import Regisseur


class TypeValeurInactive(models.Model):
    nature = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nature}"


class StockValeurInactive(models.Model):
    type_valeur = models.ForeignKey(TypeValeurInactive, on_delete=models.CASCADE)
    regisseur = models.ForeignKey(Regisseur, on_delete=models.CASCADE)
    valeur_unitaire = models.FloatField()
    nombre_de_feuillets = models.PositiveIntegerField()
    montant_total = models.IntegerField(default=0)
    date_enregistrement = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.type_valeur.nature} - {self.nombre_de_feuillets} feuillets"
