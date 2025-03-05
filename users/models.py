from django.db import models
#hachage du mot de pass
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Boutiquier(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hashed = models.CharField(max_length=255)  # Stocker le mot de passe haché

    def set_password(self, raw_password):
        """Hache le mot de passe et l'enregistre"""
        self.password_hashed = make_password(raw_password)

    def check_password(self, raw_password):
        """Vérifie si le mot de passe donné correspond au hachage"""
        return check_password(raw_password, self.password_hashed)

    def __str__(self):
        return self.nom