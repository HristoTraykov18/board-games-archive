from django.urls import path

from . import views

urlpatterns = [
    path("", views.dale_of_merchants_view, name="dale_of_merchants"),
]
