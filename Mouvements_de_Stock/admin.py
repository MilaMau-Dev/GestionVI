from django.contrib import admin
from .models import Depot, Demande


class DepotAdmin(admin.ModelAdmin):
    list_display = (
        'type_valeur', 'regisseur', 'valeur_unitaire', 'nombre_de_feuillets', 'montant_total', 'date_depot')
    search_fields = ['type_valeur__nature', 'regisseur__nom_complet', 'valeur_unitaire', 'nombre_de_feuillets',
                     'montant_total', 'date_depot']


admin.site.register(Depot, DepotAdmin)


class DemandeAdmin(admin.ModelAdmin):
    list_display = (
        'valeur_inactive', 'regisseur', 'quantite', 'date_demande', 'motif', 'statut')
    search_fields = ['valeur_inactive__type_valeur__nature', 'regisseur__nom_complet', 'quantite', 'date_demande', 'motif', 'statut']


admin.site.register(Demande, DemandeAdmin)
