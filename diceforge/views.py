from django.http import HttpResponse
from django.shortcuts import render


def dice_forge_view(request):
    return HttpResponse("Dice Forge")
