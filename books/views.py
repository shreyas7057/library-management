from django.shortcuts import redirect, render
from .models import Author,Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='login_user')
def view_author(request):
    authors = Author.objects.all()
    context = {
        'authors':authors,
    }
    return render(request,'books/view_author.html',context)


@login_required(login_url='login_user')
def add_author(request):
    if request.method=="POST":
        name = request.POST.get('name')  
        phone = request.POST.get('phone') 
        country = request.POST.get('country') 

        author = Author(
            name = name,phone=phone,country=country
        )
        author.save()
        messages.success(request,'Author Details added!')
        return redirect('view_author')

    return render(request,'books/add_author.html')


@login_required(login_url='login_user')
def edit_author(request,id):
    author = Author.objects.get(id=id)

    context = {
        'author':author,
    }
    return render(request,'books/edit_author.html',context)


@login_required(login_url='login_user')
def update_author(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        id = request.POST.get('id')

        author = Author.objects.get(id=id)
        author.name = name
        author.phone = phone
        author.country = country
        author.save()
        messages.success(request,'Author successfully edited!!')
        return redirect('view_author')

    return render(request,'books/edit_author.html')


@login_required(login_url='login_user')
def delete_author(request,id):
    author = Author.objects.get(id=id)
    author.delete()
    messages.success(request,'Author deleted successfully')
    return redirect('view_author')



def view_books(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'books/view_books.html',context)


@login_required(login_url='login_user')
def add_book(request):
    author = Author.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')  
        isbn = request.POST.get('isbn') 
        category = request.POST.get('category') 
        stock = request.POST.get('stock') 
        author_id = request.POST.get('author_id')

        author = Author.objects.get(id=author_id)

        book = Book(
            name = name,isbn=isbn,author=author,category=category,stock=stock
        )
        book.save()
        messages.success(request,'Books Details added!')
        return redirect('view_books')

    context = {
        'author':author
    }

    return render(request,'books/add_books.html',context)



@login_required(login_url='login_user')
def edit_book(request,id):
    book = Book.objects.get(id=id)
    author = Author.objects.all()

    context = {
        'book':book,
        'author':author,
    }
    return render(request,'books/edit_book.html',context)


@login_required(login_url='login_user')
def update_book(request):
    
    if request.method == "POST":
        book_id = request.POST.get('book_id')

        name = request.POST.get('name')
        isbn = request.POST.get('isbn')
        author_id = request.POST.get('author_id')
        category = request.POST.get('category')
        stock = request.POST.get('stock')

        book = Book.objects.get(id=book_id)
        book.name = name
        book.isbn = isbn
        book.category = category
        book.stock = stock

        author = Author.objects.get(id=author_id)
        book.author = author

        book.save()
        messages.success(request,'Book successfully edited!!')
        return redirect('view_books')

    return render(request,'books/edit_book.html')


@login_required(login_url='login_user')
def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Book Deleted Successfully')
    return redirect('view_books')