from django.contrib import admin
from figureprojectapp.models import Biographie, Calendrier, Contact, Image, Oeuvre, Lien, Langue

# Register your models here.

class BiographieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'texte')

class CalendrierAdmin(admin.ModelAdmin):
    list_display = ('date', 'lieu', 'oeuvre')

class LienAdmin(admin.ModelAdmin):
    list_display = ('domaine', 'nom')

admin.site.register(Biographie, BiographieAdmin)
admin.site.register(Calendrier, CalendrierAdmin)
admin.site.register(Contact)
admin.site.register(Lien, LienAdmin)
admin.site.register(Image)
admin.site.register(Langue)
admin.site.register(Oeuvre)