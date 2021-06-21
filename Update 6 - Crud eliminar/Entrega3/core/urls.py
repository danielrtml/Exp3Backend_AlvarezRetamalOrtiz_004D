from django.urls import path
from .views import Index, del_feedback, galeria, contactenos, api, mod_feedback, registro, whorwe, inise, news, feedback, mod_feedback,del_feedback
urlpatterns = [

    path('', Index, name="Index"),
    path('contactenos', contactenos, name="contactenos"),
    path('galeria', galeria, name="galeria"),
    path('api', api, name="api"),
    path('registro', registro, name="registro"),
    path('who-r-we', whorwe, name="who-r-we"),
    path('ini-se', inise, name="ini-se"),
    path('news', news, name="news"),
    path('feedback', feedback, name="feedback"),
    path('mod_feedback/<id>', mod_feedback, name="mod_feedback"),
    path('del_feedback<id>', del_feedback, name="del_feedback")

    #metodos
]