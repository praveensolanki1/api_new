from django.db import models


class BooksAuthor(models.Model):
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'books_author'
    def __str__(self) -> str:
        return self.name

class BooksFormat(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
  

    class Meta:
        managed = True
        db_table = 'books_format'
    def __str__(self) -> str:
       return self.mime_type

class BooksLanguage(models.Model):
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        managed = True
        db_table = 'books_language'

    def __str__(self) -> str:
        return self.code    
    
class BooksBook(models.Model):
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True)
    author = models.ForeignKey(BooksAuthor,on_delete=models.CASCADE,null=True,blank=True)
    format = models.ForeignKey(BooksFormat,on_delete= models.CASCADE,null=True,blank=True)
    language = models.ForeignKey(BooksLanguage,on_delete= models.CASCADE,null=True,blank=True)
    

    class Meta:
        ordering = ['-download_count']
        managed = True
        db_table = 'books_book'
    def __str__(self) -> str:
        return self.title

class BooksBookAuthors(models.Model):
    book = models.ForeignKey(BooksBook, models.DO_NOTHING)
    author = models.ForeignKey(BooksAuthor, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'books_book_authors'
        unique_together = (('book', 'author'),)

    def __str__(self) -> str:
        return self.author   
class BooksBookBookshelves(models.Model):
    book = models.ForeignKey(BooksBook, models.DO_NOTHING)
    bookshelf = models.ForeignKey('BooksBookshelf', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'books_book_bookshelves'
        unique_together = (('book', 'bookshelf'),)
   
    def __str__(self) -> str:
        return self.bookshelf 

class BooksBookLanguages(models.Model):
    book = models.ForeignKey(BooksBook, models.DO_NOTHING)
    language = models.ForeignKey('BooksLanguage', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'books_book_languages'
        unique_together = (('book', 'language'),)

    def __str__(self) -> str:
        return self.language  


class BooksBookSubjects(models.Model):
    book = models.ForeignKey(BooksBook, models.DO_NOTHING)
    subject = models.ForeignKey('BooksSubject', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'books_book_subjects'
        unique_together = (('book', 'subject'),)
    
    def __str__(self) -> str:
        return self.subject  

class BooksBookshelf(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = True
        db_table = 'books_bookshelf'

    def __str__(self) -> str:        
        return self.name 






class BooksSubject(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'books_subject'
    def __str__(self) -> str:
        return self.name 