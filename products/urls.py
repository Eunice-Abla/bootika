from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('Home/', views.Accueil, name='accueil'),  # Ajoutez un nom pour la route
    path('listes/', views.listeproduit, name='listeproduits'),  
    path('apropos/', views.apropos, name='apropos'),  
    path('contact/', views.contact, name='contact'),  
    path('ajoutCategorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('ajoutProduit/', views.ajouter_produit, name='ajouter_produit'),
    path('ajouterCategorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('listeCategories/', views.liste_categories, name='liste_categories')
]