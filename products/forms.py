# formulaire django qui serons utilisé pour saisir les données
from django import forms
from products.models import Categorie, Produit
from users.models import Boutiquier

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom_categorie', 'description']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom_prod', 'prix', 'statut', 'quantite_en_stock', 'categorie', 'boutiquier', 'image']