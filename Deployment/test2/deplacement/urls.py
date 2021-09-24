
from django.conf.urls import url
from . import views
app_name='deplacement'




urlpatterns = [
   
    url(r'^$', views.liste, name='liste'),
    url(r'^nouveau$', views.nouveau, name='nouveau'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
    url(r'^internal$', views.internal, name='internal'),

    
   
]