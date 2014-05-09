from django.conf.urls import patterns, include, url
from mysite.views import hello, home_page, current_datetime, hours_ahead
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^hello/$', hello),
   url(r'^home/$', home_page),
   url(r'^time/$', current_datetime),
   url(r'^admin/', include(admin.site.urls)),
   #Modifique el parametro de la expresion regular para probar hasta con 3 numeros
   url(r'^time/plus/(\d{1,3})/$', hours_ahead),
)
