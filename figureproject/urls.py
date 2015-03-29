from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'figureproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # format : url(r'expression.rationnelle', 'nom.de.la.vue(fonction)', nom.d.url)

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'figureproject.views.home', name='home'),
    url(r'^', include('figureprojectapp.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)