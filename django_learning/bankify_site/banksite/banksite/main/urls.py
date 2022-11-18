from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("importcsv/", views.importcsv, name="importcsv"),
    path("sorted/", views.sorted, name="sorted")
]
