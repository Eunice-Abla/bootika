from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'interface d'administration Django
    path('homebootika/', include('products.urls')),  # Inclure les URLs de l'application "products"
]

# Ajouter la gestion des fichiers média uniquement en mode DEBUG (développement)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)