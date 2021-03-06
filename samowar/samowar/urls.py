"""samowar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_stories.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('new', new_person),
    path('showAll', show_all),
    path('delete/<id>', delete),
    path('show/<id>', show_person),
    path('show/<id>/modify', modify_person),
    path('show/<id>/addAddress', add_address),
    path('show/<id>/addPhone', add_phone),
    path('show/<id>/addMail', add_mail),
    path('show/<id>/addGroup', assign_group),
    path('search-group', search_group),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
