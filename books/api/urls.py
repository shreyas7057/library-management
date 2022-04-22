from django.urls import path

from .viewsets import books_api,author_api

urlpatterns = [
    path('',books_api),
    path('author/',author_api),
]