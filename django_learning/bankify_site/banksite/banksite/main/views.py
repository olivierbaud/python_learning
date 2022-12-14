from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import CsvUploadForm, NewCategoryForm, SelectCategoryForm
from .models import Operations, Categories, Keywords
import csv
from datetime import datetime
# Create your views here.


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
                            category="",
                            categorie=Categories.objects.get(name='unknown')
                        )
                        operation.save()  
                    except:
                        pass          
            return render(request, 'main/sorted.html', {})
    else:
        form = CsvUploadForm()
    return render(request, 'main/csv.html', {"form":form})

def index(request):
    if request.method == "GET":
        for operation in Operations.objects.all():
            for word in Keywords.objects.all():
                if word.keyword in operation.memo:
                    operation.categorie = Categories.objects.get(name=word.category)
                    operation.save()
    else:
        for operation in Operations.objects.all():
            operation.categorie = Categories.objects.get(name='unknown')
            operation.save()
    return render(request, 'main/sorted.html', {
        'operations': Operations.objects.all().order_by('date'), 
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
    forbidden_words = ["card", "7152", "christchurch"]
    keyword_memo = []
    for word in operation.memo.split():
        if len(word) > 2 and word not in forbidden_words:
            keyword_memo.append(word)
         
    
    if request.method == 'POST':
        if 'selectcategoryhidden' in request.POST:
            formcategory = SelectCategoryForm(data=request.POST, keywordmemo=keyword_memo)
            if formcategory.is_valid():
                operation.categorie = Categories.objects.get(name=formcategory.cleaned_data['category'])
                operation.save()
                newkeyword=Keywords(keyword=formcategory.cleaned_data['keywords'], category=Categories.objects.get(name=operation.categorie))
                newkeyword.save()
                return render(request, 'main/operation.html', {
                    'operation':operation, 
                    'categories': Categories.objects.all(), 
                    'keyword_memo': keyword_memo,
                    'form': NewCategoryForm(),
                    'formcategory': SelectCategoryForm(keywordmemo=keyword_memo),
                    'succes': True
                    })
            else:
                print("error", formcategory.errors.as_data())
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
        formcategory = SelectCategoryForm(keywordmemo=keyword_memo)

    return render(request, 'main/operation.html', {
        'operation':operation, 
        'categories': Categories.objects.all(), 
        'keyword_memo': keyword_memo,
        'form': NewCategoryForm(),
        'formcategory': SelectCategoryForm(keywordmemo=keyword_memo),
        })

#def popup(request):
 #   return HttpResponseRedirect(reverse('operation'))
