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
from django.contrib import admin
from django.urls import path

# from First_app.views import home_view, contacts_view, my_description_view, form_create_view, django_form_view, my_decription_dynamic_view, delete_object_view,descr_list_view
from First_app.views import (
    firstapp_descr_list_view,
    firstapp_home_view,
    firstapp_contacts_view,
    firstapp_my_description_view,
    firstapp_form_create_view,
    firstapp_django_form_view,
    firstapp_my_decription_dynamic_view,
    firstapp_delete_object_view,
)
urlpatterns = [
    path('', firstapp_home_view, name="home" ),
    path('firstapp/contacts/', firstapp_contacts_view, name="contacts"),
    path('firstapp/onedescr/', firstapp_my_description_view, name="descr"),
    path('firstapp/<int:my_id>/', firstapp_my_decription_dynamic_view, name="descr-detail"),
    path('firstapp/', firstapp_descr_list_view, name="descr-list"),
    path('firstapp/form/', firstapp_form_create_view, name="form"),
    path('firstapp/djangoform/', firstapp_django_form_view, name="django-form"),
    path('firstapp/deleteobject/<int:my_id>/', firstapp_delete_object_view, name="delete-object" ),
    path('admin/', admin.site.urls),
]
