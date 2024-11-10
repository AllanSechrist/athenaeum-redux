from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "book_list"

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"
    
