from django.urls import path
from .views import inicio, galeria, contactenos, api, registro, whorwe, inise, news
urlpatterns = [

    path('', inicio, name="inicio"),
    path('contactenos', contactenos, name="contactenos"),
    path('galeria', galeria, name="galeria"),
    path('api', api, name="api"),
    path('registro', registro, name="registro"),
    path('who-r-we', whorwe, name="who-r-we"),
    path('ini-se', inise, name="ini-se"),
    path('news', news, name="news"),
]