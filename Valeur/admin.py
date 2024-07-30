from django.contrib import admin
from .models import TypeValeurInactive, StockValeurInactive


class TypeValeurInactiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'nature')
    search_fields = ['id', 'nature']


admin.site.register(TypeValeurInactive, TypeValeurInactiveAdmin)


class StockValeurInactiveAdmin(admin.ModelAdmin):
    list_display = ('type_valeur', 'regisseur', 'valeur_unitaire', 'nombre_de_feuillets', 'montant_total', 'date_enregistrement')
    search_fields = ['type_valeur__nature', 'regisseur__nom_complet', 'valeur_unitaire', 'nombre_de_feuillets', 'montant_total', 'date_enregistrement']


admin.site.register(StockValeurInactive, StockValeurInactiveAdmin)
