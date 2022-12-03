from django.urls import path
from . import views

urlpatterns = [
    path("", views.sorted, name="index"),
    path("importcsv/", views.importcsv, name="importcsv"),
    path("sorted/", views.sorted, name="sorted"),
    path("categories/", views.categories, name="categories"),
    path("<int:id>", views.operation, name="operation"),
    
]
