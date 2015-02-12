from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

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
    url = models.URLField(blank=True)
    langue = models.ForeignKey('Langue')


class Contact(models.Model):
    domaine = models.CharField(max_length=200, blank=True)
    entite = models.CharField(max_length=200, blank=True)
    nom = models.CharField(max_length=200, blank=True)
    adresse = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(blank=True)
    langue = models.ForeignKey('Langue')

    def __unicode__(self):
        return '[%s] %s' % (self.langue, self.domaine)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    oeuvre = models.ForeignKey('Oeuvre')


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
    titre_oeuvre = models.CharField(max_length=200)
    note = models.TextField()
    mentions = models.TextField()
    distribution = models.TextField()
    diffusion = models.TextField(blank=True)
    image_titre = models.ImageField(upload_to='images_titre')
    typo_titre = models.ImageField(upload_to='images_titre')
    langue = models.ForeignKey('Langue')
    slug = models.SlugField(default='slug-non-configure')

    def __unicode__(self):
        return '[%s] %s' % (self.langue, self.titre_oeuvre)

    def get_absolute_url(self):
        return reverse('oeuvre', kwargs={'slug': self.slug})
#   kwargs = arguments nommes
#   args = arguments ordonnes


class Langue(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    langue = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code