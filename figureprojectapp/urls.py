from django.conf.urls import patterns, url
from figureprojectapp import views

urlpatterns = patterns('',
    url(r'^/?$', views.oeuvres, name='home'),
    url(r'^biographie/', views.biographie, name='biographie'),
    url(r'^#oeuvres/', views.oeuvres, name='oeuvres'),
    url(r'^oeuvre/(?P<slug>[a-z0-9-_]+)', views.oeuvre, name='oeuvre'),
    url(r'^extension-sauvage/', views.extensionsauvage, name='extensionsauvage'),
    url(r'^#calendrier/', views.calendrier, name='calendrier'),
    url(r'^liens/', views.liens, name='liens'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^en/biography/', views.biography, name='biography'),
    url(r'^en/works/', views.works, name='works'),
    url(r'^en/work/(?P<slug>[a-z0-9-_]+)', views.work, name='work'),
    url(r'^en/extension-sauvage/', views.extensionsauvageen, name='extensionsauvageen'),
    url(r'^en/calendar/', views.calendar, name='calendar'),
    url(r'^en/links/', views.links, name='links'),
    url(r'^en/contact/', views.contacten, name='contacten'),
)
# exp ration. + nom de la vue (fonction) + nom
