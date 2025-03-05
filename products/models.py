from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)
    description = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.nom_categorie

class Produit(models.Model):
    CHOIX_STATUT = [
        ('disponible', 'Disponible'),
        ('indisponible', 'Indisponible')
    ]

    nom_prod = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=15, decimal_places=2)
    statut = models.CharField(max_length=14, choices=CHOIX_STATUT, default='indisponible')
    quantite_en_stock = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    boutiquier = models.ForeignKey('users.Boutiquier', on_delete=models.CASCADE)  # Relation avec le boutiquier
    image = models.ImageField(upload_to='produits/', null=True, blank=True)  # Nouveau champ pour les images
    def __str__(self):
        return self.nom_prod