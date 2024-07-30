from django.contrib import admin
from .models import Commune


class CommuneAdmin(admin.ModelAdmin):
    list_display = ('code_commune', 'nom', 'mail', 'adresse')
    search_fields = ['code_commune', 'nom', 'mail', 'adresse']


admin.site.register(Commune, CommuneAdmin)
