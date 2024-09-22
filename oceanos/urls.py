from django.urls import path

from . import views

urlpatterns = [
    path("", views.oceanos_view, name="oceanos"),
]
