"""Entrega3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('contactenos', include('core.urls')),
    path('galeria', include('core.urls')),
    path('registro', include('core.urls')),
    path('who-r-we', include('core.urls')),
    path('ini-se', include('core.urls')),
    path('news', include('core.urls')),
    path('feedback', include('core.urls')),
    path('home', include('core.urls')),
]
