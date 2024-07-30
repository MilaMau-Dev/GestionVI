from datetime import date

from django.db import models
from Regisseur.models import Regisseur
from Valeur.models import TypeValeurInactive, StockValeurInactive


class Depot(models.Model):
    type_valeur = models.ForeignKey(TypeValeurInactive, on_delete=models.CASCADE)
    regisseur = models.ForeignKey(Regisseur, on_delete=models.CASCADE)
    valeur_unitaire = models.FloatField()
    nombre_de_feuillets = models.PositiveIntegerField()
    montant_total = models.IntegerField(default=0)
    date_depot = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.type_valeur.nature} - {self.nombre_de_feuillets} feuillets déposé par {self.regisseur.nom_complet}"


class Demande(models.Model):
    valeur_inactive = models.ForeignKey(StockValeurInactive, on_delete=models.CASCADE)
    regisseur = models.ForeignKey(Regisseur, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    motif = models.TextField(blank=True)
    date_demande = models.DateField(default=date.today)
    statut = models.CharField(max_length=20,
                              choices=[('en attente', 'En attente'),
                                       ('approuvée', 'Approuvée'),
                                       ('rejetée', 'Rejetée')])

    def __str__(self):
        return f"{self.valeur_inactive.type_valeur.nature} - {self.quantite} feuillets demandé par {self.regisseur.nom_complet}"
