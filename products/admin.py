from django.contrib import admin
from .models import Produit
from .models import Categorie
# Register your models here.

admin.site.register(Produit)
admin.site.register(Categorie)