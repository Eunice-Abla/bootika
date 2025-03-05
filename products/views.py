from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from products.forms import CategorieForm, ProduitForm
from products.models import Produit, Categorie
from users.models import Boutiquier

# Create your views here.
def Accueil(request):
    return render(request, "accueil.html")
def listeproduit(request):
    listes= Produit.objects.all()
    return render(request, "listeproduits.html", {'listes':listes})
def liste_categories(request):
    categories = Categorie.objects.all()  # Récupérer toutes les catégories
    return render(request, 'liste_categories.html', {'categories': categories})
def apropos(request):
    return render(request, "apropos.html")
def contact(request):
    errors = []
    if request.method == 'POST':
        nom = request.POST.get('nom').strip()
        email = request.POST.get('email').strip()
        message = request.POST.get('message').strip()

        # Vérifier si les champs sont remplis
        if not nom:
            errors.append("Le nom est requis.")
        if not email:
            errors.append("L'email est requis.")
        if not message:
            errors.append("Le message est requis.")
        # Valider le format de l'email avec une expression régulière
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if email and not re.match(email_regex, email):
            errors.append("L'adresse email n'est pas valide.")
        # Vérifier la longueur du message
        if message and len(message) < 10:
            errors.append("Le message est trop court. (min. 10 caractères)")
        if message and len(message) > 1000:
            errors.append("Le message est trop long. (max. 1000 caractères)")
        # Si des erreurs sont présentes, on les renvoie au template
        if errors:
            return render(request, 'contact.html', {'errors': errors})
        # Si tout est bon, on peut traiter le message (ex : l'enregistrer ou l'envoyer)
        print(f"Message de {nom} ({email}) : {message}")
        return HttpResponse("<h2>Merci pour votre message ! Nous vous répondrons bientôt.</h2>")
    return render(request, 'contact.html')

#si nous avons des insertion 
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')  # Redirige vers une page de liste des catégories
    #si non il affiche la page d'ajout
    else:
        form = CategorieForm()
    return render(request, 'ajouter_categorie.html', {'form': form})

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)  # request.FILES pour gérer l'upload d'images
        if form.is_valid():
            form.save()
            return redirect('listeproduits')  # Redirige vers une page de liste des produits
    else:
        form = ProduitForm()
    return render(request, 'ajouter_produit.html', {'form': form})