from django.urls import path

from . import views

urlpatterns = [
    path("", views.unmatched_view, name="unmatched"),
]
