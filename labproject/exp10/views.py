from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'publication_date', 'authors', 'publisher']
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title', 'publication_date', 'authors', 'publisher']
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')   