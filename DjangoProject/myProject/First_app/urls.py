from django.urls import path

from .views import (
    firstapp_descr_list_view,
    firstapp_my_description_view,
    firstapp_form_create_view,
    firstapp_django_form_view,
    firstapp_my_decription_dynamic_view,
    firstapp_delete_object_view,
)


app_name = "first_app"

urlpatterns = [
    path('onedescr/', firstapp_my_description_view, name="descr"),
    path('list/<int:my_id>/', firstapp_my_decription_dynamic_view, name="descr-detail"),
    path('list/', firstapp_descr_list_view, name="descr-list"),
    path('form/', firstapp_form_create_view, name="form"),
    path('djangoform/', firstapp_django_form_view, name="django-form"),
    path('<int:my_id>/delete/', firstapp_delete_object_view, name="delete-object" ),
]