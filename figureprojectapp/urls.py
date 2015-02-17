from django.conf.urls import patterns, url
from figureprojectapp import views

urlpatterns = patterns('',
    url(r'^/?$', views.home, name='home'),
    url(r'^biographie/', views.biographie, name='biographie'),
    url(r'^#oeuvres/', views.home, name='oeuvres'),
    url(r'^oeuvre/(?P<slug>[a-z0-9-_]+)', views.oeuvre, name='oeuvre'),
    url(r'^extension-sauvage/', views.extensionsauvage, name='extensionsauvage'),
    url(r'^calendrier/', views.calendrier, name='calendrier'),
    url(r'^liens/', views.liens, name='liens'),
    url(r'^contact/', views.contact, name='contact'),
)
# exp ration. + nom de la vue (fonction) + nom
