from django.contrib import admin
from .models import Regisseur


class RegisseurAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'email', 'commune', 'telephone')
    search_fields = ['nom_complet', 'email', 'commune__nom', 'telephone']


admin.site.register(Regisseur, RegisseurAdmin)
