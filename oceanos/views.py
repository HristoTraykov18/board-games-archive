from django.http import HttpResponse
from django.shortcuts import render


def oceanos_view(request):
    return HttpResponse("Oceanos")
