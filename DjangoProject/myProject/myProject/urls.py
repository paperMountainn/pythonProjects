"""myProject URL Configuration

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
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# from First_app.views import home_view, contacts_view, my_description_view, form_create_view, django_form_view, my_decription_dynamic_view, delete_object_view,descr_list_view

urlpatterns = [
    path('firstapp/', include('First_app.urls')),
    path('', include('Main.urls')),
    
    path('admin/', admin.site.urls),
]
