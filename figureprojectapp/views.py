# -*- coding: utf-8 -*-
from django.shortcuts import render
from figureprojectapp.models import Oeuvre, Biographie, Lien, Contact, Calendrier, Projet, Image, Atelier, Actualite

# Create your views here.
# filter pour fr/en
# variable, internationalisation

def oeuvres(request):
    oeuvres = Oeuvre.objects.filter(langue='fr').all()
    actu = Actualite.objects.filter(langue='fr').get()
    return render(request, 'index.html', {'oeuvres': oeuvres, 'actu':actu})
    # objet request + template + contexte cad les variables qui seront disponibles dans le template

def oeuvre(request, slug):
    oeuvres = Oeuvre.objects.filter(langue='fr').all()
    objet_oeuvre = Oeuvre.objects.select_related().filter(langue="fr").get(slug=slug)
    img_oeuvre = objet_oeuvre.image_set.all()
    dates = objet_oeuvre.calendrier_set.all()
    next_oeuvre = Oeuvre.objects.filter(id__gt=objet_oeuvre.id).first()
    prev_oeuvre = Oeuvre.objects.filter(id__gt=objet_oeuvre.id).first()
#   1er slug : paramètre nomme, 2eme : variable fournie a def
    return render(request, 'oeuvre.html', {'oeuvre': objet_oeuvre, 'img_oeuvre':img_oeuvre, 'dates':dates, 'next': next_oeuvre, 'prev': prev_oeuvre, 'oeuvres': oeuvres})

def biographie(request):
    biographie = Biographie.objects.filter(langue='fr').all()
    return render(request, 'biographie.html', {'biographie': biographie})
# , 'formfr':formfr, 'defigurerfr':defigurerfr, 'detournerfr':detournerfr, 'deplacerfr':deplacerfr

def extensionsauvage(request):
    extsauvage = Projet.objects.select_related('image').filter(langue="fr").get(titre='Extension sauvage')
    i_es = extsauvage.image_set.all()
    return render(request, 'extension-sauvage.html', {'extsauvage': extsauvage, 'i_es': i_es})

def calendrier(request, year):
    calendriers_menu = Calendrier.objects.select_related('oeuvre').all()
    if year == None:
        calendriers = calendriers_menu
    else:
        calendriers = [ calendrier for calendrier in calendriers_menu if calendrier.date.year == int(year) ]

    return render(request, 'calendrier.html', {'dates': calendriers, 'calendriers_menu': calendriers_menu})

def contact(request):
    contacts = Contact.objects.filter(langue="fr").all()
    return render(request, 'contact.html', {'contacts': contacts})

def liens(request):
    liens_partcult = Lien.objects.filter(domaine='Partenaires culturels')
    liens_parteduc = Lien.objects.filter(domaine='Partenaires éducatifs')
    liens_artistes = Lien.objects.filter(domaine='Artistes')
    liens_utiles = Lien.objects.filter(domaine='Liens utiles')
    return render(request, 'liens.html', {'liens_partcult': liens_partcult, 'liens_parteduc': liens_parteduc, 'liens_artistes': liens_artistes, 'liens_utiles': liens_utiles})

def actualite(request):
    actu = Actualite.objects.filter(langue='fr').get(statut_objet='actif')
    return render(request, 'actu.html', {'actu': actu})

def works(request):
    oeuvres = Oeuvre.objects.filter(langue='en').all()
    return render(request, 'works.html', {'oeuvres': oeuvres})

def work(request, slug):
    object_work = Oeuvre.objects.select_related().filter(langue="en").get(slug=slug)
    img_oeuvre = object_work.image_set.all()
    dates = object_work.calendrier_set.all()
#    next_work = Oeuvre.objects.filter(id__gt=object_work.id).first()
#    prev_work = Oeuvre.objects.filter(id__gt=object_work.id).first()
#   1er slug : paramètre nomme, 2eme : variable fournie a def
    return render(request, 'work.html', {'oeuvre': object_work, 'img_oeuvre':img_oeuvre, 'dates':dates})

def links(request):
    liens_partcult = Lien.objects.filter(domaine='Partenaires culturels')
    liens_parteduc = Lien.objects.filter(domaine='Partenaires éducatifs')
    liens_artistes = Lien.objects.filter(domaine='Artistes')
    liens_utiles = Lien.objects.filter(domaine='Liens utiles')
    return render(request, 'links.html', {'liens_partcult': liens_partcult, 'liens_parteduc': liens_parteduc, 'liens_artistes': liens_artistes, 'liens_utiles': liens_utiles})

def biography(request):
    biographie = Biographie.objects.filter(langue='en').all()
    return render(request, 'biography.html', {'biographie': biographie})

def extensionsauvageen(request):
    extsauvage = Projet.objects.select_related('image').filter(langue="en").get(titre='Extension sauvage')
    i_es = extsauvage.image_set.all()
    return render(request, 'extension-sauvage-en.html', {'extsauvage': extsauvage, 'i_es': i_es})

def calendar(request):
    dates = Calendrier.objects.select_related('oeuvre').all()
    return render(request, 'calendar.html', {'dates': dates})

def contacten(request):
    contacts = Contact.objects.filter(langue="en").all()
    return render(request, 'contacten.html', {'contacts': contacts})