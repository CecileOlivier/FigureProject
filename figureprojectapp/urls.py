from django.conf.urls import patterns, url
from figureprojectapp import views

urlpatterns = patterns('',
    url(r'^/?$', views.home, name='home'),
    url(r'^biographie/', views.biographie, name='biographie'),
    url(r'^oeuvres/', views.oeuvres, name='oeuvres'),
    url(r'^oeuvre/', views.oeuvre, name='oeuvre'),
    url(r'^extension-sauvage/', views.extensionsauvage, name='extensionsauvage'),
    url(r'^calendrier/', views.calendrier, name='calendrier'),
    url(r'^liens/', views.liens, name='liens'),
    url(r'^contact/', views.contact, name='contact'),
)
# exp ration. + nom de la vue (fonction) + nom
