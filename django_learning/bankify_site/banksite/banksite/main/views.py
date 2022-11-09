from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("bankify site")

def import_csv(response):
    return HttpResponse(response, "main/import_csv.html", {})

