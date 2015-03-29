from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

TYPE_CHOICES = (('oeuvre', 'oeuvre'),
                ('atelier', 'atelier'))

class Biographie(models.Model):
    titre = models.CharField(max_length=200, blank=True)
    texte = models.TextField()
    langue = models.ForeignKey('Langue')

    def __unicode__(self):
        return '[%s] %s - %s' % (self.langue, self.titre, self.texte)


class Calendrier(models.Model):
    date = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    cadre = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    oeuvre = models.ForeignKey('Oeuvre', blank=True, null=True)
    atelier = models.ForeignKey('Atelier', blank=True, null=True)
    langue = models.ForeignKey('Langue')
    type_objet = models.CharField(max_length=7, choices=TYPE_CHOICES);

    def __unicode__(self):
        return '[%s] %s %s %s' % (self.langue, self.date, self.lieu, self.oeuvre)

    def objet(self):
        return getattr(self, self.type_objet)


class Contact(models.Model):
    domaine = models.CharField(max_length=200, blank=True)
    entite = models.CharField(max_length=200, blank=True)
    nom = models.CharField(max_length=200, blank=True)
    adresse = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(blank=True)
    langue = models.ForeignKey('Langue')

    def __unicode__(self):
        return '[%s] %s - %s %s' % (self.langue, self.domaine, self.entite, self.nom)


class Lien(models.Model):
    domaine = models.CharField(max_length=200)
    url = models.URLField()
    nom = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(blank=True)
    description = models.CharField(max_length=200, blank=True)
    langue = models.ForeignKey('Langue')

    def __unicode__(self):
        return '[%s] [%s] %s' % (self.langue, self.domaine, self.nom)


class Oeuvre(models.Model):

    def visuel(self):
        return '<img src="%s" width="auto" height="50"/>' % self.image_titre.url
    visuel.allow_tags = True

    titre_oeuvre = models.CharField(max_length=200)
    note = models.TextField()
    mentions = models.TextField()
    distribution = models.TextField()
    image_titre = models.ImageField(upload_to='images_titre')
    typo_titre = models.ImageField(upload_to='images_titre')
    langue = models.ForeignKey('Langue')
    slug = models.SlugField(default='slug-non-configure')

    def __unicode__(self):
        return u'[%s] %s' % (self.langue, self.titre_oeuvre)


#   kwargs = arguments nommes
#   args = arguments ordonnes
    def get_absolute_url(self):
        if self.langue.code == 'fr':
            return reverse('oeuvre', kwargs={'slug': self.slug})
        else:
            return reverse('work', kwargs={'slug': self.slug})


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    image_titre_desktop = models.ImageField(upload_to='images_titre')
    image_titre_mobile = models.ImageField(upload_to='images_titre')
    note = models.TextField()
    info = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    langue = models.ForeignKey('Langue')

    def __unicode__(self):
        return '[%s] %s' % (self.langue, self.titre)


class Image(models.Model):

    image = models.ImageField(upload_to='images')
    projet = models.ManyToManyField(Projet, blank=True, null=True)
    oeuvre = models.ManyToManyField(Oeuvre, blank=True, null=True)
#    oeuvre = models.ForeignKey('Oeuvre', blank=True, null=True)
#    projet = models.ForeignKey('Projet', blank=True,  null=True)

    def visuel(self):
        return '<img src="%s" width="auto" height="50"/>' % self.image.url
    visuel.allow_tags = True

    def __unicode__(self):
        return u'%s' % (self.image)


class Atelier(models.Model):
    titre = models.CharField(max_length=200)
    typo_titre = models.ImageField(upload_to='images_titre')
    langue = models.ForeignKey('Langue')

    def __unicode__(self):
        return '[%s] %s' % (self.langue, self.titre)


class Langue(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    langue = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code


class Actualite(models.Model):
    STATUS_CHOICES = (('actif', 'actif'),
                    ('inactif', 'inactif'))
    titre = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    texte = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    logo = models.ImageField(upload_to='images', blank=True, null=True)
    statut_objet = models.CharField(max_length=7, choices=STATUS_CHOICES, default='inactif')
    langue = models.ForeignKey('Langue')

#    def __unicode__(self):
#        return '[%s] %s %s' % (self.langue, self.titre, self.statut_objet)

    def objet(self):
        return getattr(self, self.statut_objet)