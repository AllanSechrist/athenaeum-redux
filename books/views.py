from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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

class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "publisher", "isbn"]
    template_name = "add_book.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        return super().form_valid(form)

