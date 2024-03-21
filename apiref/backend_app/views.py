from django.shortcuts import render
from . models import *
from rest_framework import generics
from . serializers import *
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):

    page_query_param = 20



class AuthorListView(generics.ListCreateAPIView):
    queryset = BooksAuthor.objects.all()
    serializer_class = BooksAuthorSerializer
    filter_backends = [
       
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['name']
    pagination_class = CustomPagination



class AuthorDetailView(generics.RetrieveAPIView):
    queryset = BooksAuthor.objects.all()
    serializer_class = BooksAuthorSerializer
    pagination_class = CustomPagination


    name = 'Author detail'


class BookListView(generics.ListCreateAPIView):
    queryset = BooksBook.objects.all().order_by('-download_count')
    serializer_class = BooksBookSerializer
    pagination_class = CustomPagination
    name = 'Books-list'
    filter_backends = [
       
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "title": ["icontains", "startswith"],
        "gutenberg_id": ["icontains",], 
        "title": ["startswith",],  
        "language": ["startswith",]  
    }


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BooksBook.objects.all()
    serializer_class = BooksBookSerializer
    pagination_class = CustomPagination

    name = 'Book-detail'

