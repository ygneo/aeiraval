from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'aeiraval_app.views.login_page'),
    url(r'^buttons/', 'aeiraval_app.views.buttons'),
    url(r'^fitxes/', 'aeiraval_app.views.fitxes'),
    url(r'^analisi/', 'aeiraval_app.views.analisi_inicial'),
    url(r'^inicial/', 'aeiraval_app.views.entrevista_inicial'),
    url(r'^inscripcio/', 'aeiraval_app.views.inscripcio'),
    url(r'^pla_de_treball/', 'aeiraval_app.views.pla_de_treball'),
    url(r'^derivacio/', 'aeiraval_app.views.derivacio'),
    url(r'^valoracio/', 'aeiraval_app.views.valoracio'),
    url(r'^informe/', 'aeiraval_app.views.informe'),
    url(r'^acord/', 'aeiraval_app.views.acord'),
#    url(r'^logout/$', 'aeiraval_app.views.logout'),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
