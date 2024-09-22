from django.http import HttpResponse
from django.shortcuts import render


def archive_view(request):
    return HttpResponse("Board Games Archive")
