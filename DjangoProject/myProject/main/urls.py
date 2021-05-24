from django.urls import path

from .views import (
    main_home_view,
    main_contacts_view,
)

urlpatterns =[
    path('', main_home_view, name="home" ),
    path('contacts/', main_contacts_view, name="contacts"),
]