from django.http import HttpResponse
from django.shortcuts import render


def unmatched_view(request):
    return HttpResponse("Unmatched")
