from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path("", BookListView.as_view() ,name="book_list"),
    path("<int:pk>", BookDetailView.as_view(), name="book_detail"),
    path("add/", BookCreateView.as_view(), name="add_book"),
    # path("<int:book_id>", views.detail, name="detail"),
]