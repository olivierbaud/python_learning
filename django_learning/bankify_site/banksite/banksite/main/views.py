from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CsvUploadForm
from .models import Operations
import csv
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'main/home.html', {})

def importcsv(request):
    if request.method == "POST":
        form = CsvUploadForm(request.POST, request.FILES )
        if form.is_valid():
            with open('main/media/test.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(float(row.get("amount")))
                    operation = Operations(
                        date=datetime.strptime(row.get("date"), '%Y/%m/%d'),
                        type=row.get("type"),
                        uniqueid=int(row.get("uniqueID")),
                        memo=row.get("memo").lower(),
                        amount=float(row.get("amount")),
                        category=""
                    )
                    operation.save()            
            return render(request, 'main/sorted.html', {})
    else:
        form = CsvUploadForm()
    return render(request, 'main/csv.html', {"form":form})

def sorted(request):
    return render(request, 'main/sorted.html', {})

