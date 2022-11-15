from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CsvUploadForm
import csv
# Create your views here.

def index(request):
    return render(request, 'main/home.html', {})

def csv(request):
    if request.method == "POST":
        form = CsvUploadForm(request.POST, request.FILES )
        if form.is_valid():
            with open(request.FILES['file']) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print('h')
            return HttpResponseRedirect('main/sorted.html')
    else:
        form = CsvUploadForm()
    return render(request, 'main/csv.html', {"form":form})

def sorted(request):
    return render(request, 'main/sorted.html', {})

