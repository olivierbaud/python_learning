from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import CsvUploadForm, NewCategoryForm, SelectCategoryForm
from .models import Operations, Categories, Keywords
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
                    try:
                        operation = Operations(
                            date=datetime.strptime(row.get("date"), '%Y/%m/%d'),
                            type=row.get("type"),
                            uniqueid=int(row.get("uniqueID")),
                            memo=row.get("memo").lower(),
                            amount=float(row.get("amount")),
                            category=""
                        )
                        operation.save()  
                    except:
                        pass          
            return render(request, 'main/sorted.html', {})
    else:
        form = CsvUploadForm()
    return render(request, 'main/csv.html', {"form":form})

def sorted(request):
    if request.method == "GET":
        for operation in Operations.objects.all():
            for word in Keywords.objects.all():
                if word.keyword in operation.memo:
                    operation.category = word.category.name
                    operation.save()
    return render(request, 'main/sorted.html', {
        'operations': Operations.objects.all().order_by('date').values(), 
        'categories': Categories.objects.all(), 
        'keywords': Keywords.objects.all()
        })

def categories(request):
    return render(request, 'main/categories.html', {
        'categories': Categories.objects.all(), 
        'keywords': Keywords.objects.all()
        })

def operation(request, id):
    operation = Operations.objects.get(uniqueid=id)
    keyword_memo = operation.memo.split()
    if request.method == 'POST':
        if 'selectcategoryhidden' in request.POST:
            form = SelectCategoryForm(request.POST)
            print(request.POST)
            if form.is_valid():
                print('test', form)
                operation.category = form.cleaned_data['categorie']
                operation.save()
                
                return render(request, 'main/operation.html', {
                    'operation':operation, 
                    'categories': Categories.objects.all(), 
                    'keyword_memo': keyword_memo,
                    'form': NewCategoryForm(),
                    'formcategory': SelectCategoryForm(keywordmemo=keyword_memo),
                    'succes': True
                    })
        else:
            form = NewCategoryForm(request.POST)
            if form.is_valid():
                new_category = Categories(name = form.cleaned_data['name'])
                new_category.save()
                return render(request, 'main/operation.html', {
                    'operation':operation, 
                    'categories': Categories.objects.all(), 
                    'keyword_memo': keyword_memo,
                    'form': NewCategoryForm(),
                    'formcategory': SelectCategoryForm(keywordmemo=keyword_memo),
                    'succes': True
                    })
    else:
        form = NewCategoryForm()
    return render(request, 'main/operation.html', {
        'operation':operation, 
        'categories': Categories.objects.all(), 
        'keyword_memo': keyword_memo,
        'form': NewCategoryForm(),
        'formcategory': SelectCategoryForm(keywordmemo=keyword_memo),
        })

#def popup(request):
 #   return HttpResponseRedirect(reverse('operation'))
