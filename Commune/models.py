from django.db import models


class Commune(models.Model):
    code_commune = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField()
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
