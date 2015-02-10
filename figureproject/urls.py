from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'figureproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # format : url(r'expression.rationnelle', 'nom.de.la.vue(fonction)', nom.d.url)

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'figureproject.views.home', name='home'),
    url(r'^', include('figureprojectapp.urls')),

)