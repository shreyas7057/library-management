from rest_framework.decorators import api_view
from .serializers import BookSerializer,AuthorSerializer
from books.models import Book,Author
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST','PATCH','DELETE'])
def author_api(request,pk=None):
    if request.method == "GET":        
        author = Author.objects.all()
        serializer = AuthorSerializer(author,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Author Details Saved'},status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk

        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(author,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Author Details updated'})

        return Response(serializer.errors)

    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        author = Author.objects.get(pk=id)
        author.delete()
        return Response({'msg':'Author deleted'})


@api_view(['GET','POST','PATCH','DELETE'])
def books_api(request,pk=None):
    if request.method == "GET":        
        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Book Details Saved'},status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk

        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Book Details updated'})

        return Response(serializer.errors)


    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        book = Book.objects.get(pk=id)
        book.delete()
        return Response({'msg':'Book deleted'})
