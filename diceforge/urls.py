from django.urls import path

from . import views

urlpatterns = [
    path("", views.dice_forge_view, name="dice_forge"),
]
