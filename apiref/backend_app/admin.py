

from django.contrib import admin
from . models import *


admin.site.register(BooksAuthor)
admin.site.register(BooksBook)
admin.site.register(BooksBookAuthors)
admin.site.register(BooksBookBookshelves)
admin.site.register(BooksBookLanguages)
admin.site.register(BooksLanguage)
admin.site.register(BooksBookSubjects)
admin.site.register(BooksSubject)
admin.site.register(BooksFormat)
admin.site.register(BooksBookshelf)