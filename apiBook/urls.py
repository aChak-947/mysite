from django.urls import path
from . import views

urlpatterns = [
    path("book_list/", views.ListBooks.as_view()),
    path("book_create/", views.UpsertBook.as_view()),
    path("book_delete/", views.DeleteBook.as_view()),
]