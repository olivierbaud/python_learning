from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("bankify site")

def csv(response):
    return render(response, 'main/csv.html', {})

