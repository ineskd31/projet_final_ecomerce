from django.shortcuts import render

# Create your views here.
def produit(request):
    return render(request, 'temp/front/produit/produit.html')