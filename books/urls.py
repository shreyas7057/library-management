from django.urls import path
from .views import add_author,edit_author, update_author,view_author,delete_author,view_books,add_book,edit_book,update_book,delete_book


urlpatterns = [
    path('author/add/',add_author,name='add_author'),
    path('author/view/',view_author,name='view_author'),
    path('author/delete/<int:id>/',delete_author,name='delete_author'),
    path('author/edit/<int:id>/',edit_author,name='edit_author'),
    path('author/update/',update_author,name='update_author'),

    path('',view_books,name='view_books'),
    path('books/add/',add_book,name='add_book'),
    path('book/edit/<int:id>/',edit_book,name='edit_book'),
    path('book/update/',update_book,name='update_book'),
    path('book/delete/<int:id>/',delete_book,name='delete_book'),

]