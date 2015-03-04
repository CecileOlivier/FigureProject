from django.contrib import admin
from figureprojectapp.models import Biographie, Calendrier, Contact, Oeuvre, Image, Lien, Langue, Projet, Atelier, Actualite

# Register your models here.

class BiographieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'texte', 'langue')
    search_fields = ['titre', 'langue']

class CalendrierAdmin(admin.ModelAdmin):
    list_display = ('date', 'lieu', 'oeuvre', 'atelier')
    search_fields = ['lieu', 'oeuvre', 'atelier']

class LienAdmin(admin.ModelAdmin):
    list_display = ('domaine', 'nom')
    search_fields = ['domaine', 'nom']
    list_filter = ('domaine', 'nom')

class ImageAdmin(admin.ModelAdmin):    
    # visuel c'est la fonction qui renvoi le code html qui va etre afficher 
    # faut aussi le mettre en 1er pour qu'il soit afficher comme lien
    list_display = ('visuel', 'image')
    search_fields = ['oeuvre', 'projet']
    list_filter = ('oeuvre', 'projet')

class OeuvreAdmin(admin.ModelAdmin):    
    list_display = ('titre_oeuvre', 'visuel', 'langue')
    search_fields = ['oeuvre', 'projet']

admin.site.register(Biographie, BiographieAdmin)
admin.site.register(Calendrier, CalendrierAdmin)
admin.site.register(Contact)
admin.site.register(Lien, LienAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Langue)
admin.site.register(Oeuvre, OeuvreAdmin)
admin.site.register(Projet)
admin.site.register(Atelier)
admin.site.register(Actualite)