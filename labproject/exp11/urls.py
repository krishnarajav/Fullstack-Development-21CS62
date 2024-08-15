from django.urls import path
from .views import hello_pdf, export_books_csv

urlpatterns = [
    path('export-csv', export_books_csv, name='export-csv'),
    path('export-pdf/', hello_pdf, name='hello_pdf'),
]