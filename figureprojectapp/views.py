from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
    # objet request + template + contexte cad les variables qui seront disponibles dans le template

def oeuvres(request):
    return render(request, 'index.html')

def oeuvre(request):
    return render(request, 'oeuvre.html')

def biographie(request):
    return render(request, 'biographie.html')

def extensionsauvage(request):
    return render(request, 'extension-sauvage.html')

def calendrier(request):
    return render(request, 'calendrier.html')

def contact(request):
    return render(request, 'contact.html')

def liens(request):
    return render(request, 'liens.html')