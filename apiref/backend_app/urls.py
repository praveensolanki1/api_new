from django.urls  import path 
from . import views 

urlpatterns = [ 
	path('authors/', views.AuthorListView.as_view(),name='author_list'),
	path('author/<pk>', views.AuthorDetailView.as_view(),name='author_detail'),
	path('books/', views.BookListView.as_view(),name='books_list'),
	path('books/<pk>', views.BookDetailView.as_view(),name='books_detail'),
] 
