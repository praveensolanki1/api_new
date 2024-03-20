from rest_framework import serializers
from . models import *





class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
       model = BooksAuthor
       fields = '__all__' 

class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = '__all__'       



class BooksBookSerializer(serializers.ModelSerializer):
    format = BooksFormatSerializer()
    class Meta:
       model = BooksBook
       fields = '__all__' 



class BooksBookAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
       model =BooksBookAuthors
       fields = '__all__' 



class BooksBookBookshelvesSerializer(serializers.ModelSerializer):
    class Meta:
       model =BooksBookBookshelves
       fields = '__all__' 


class BooksBookLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
       model = BooksBookLanguages
       fields = '__all__' 


class BooksBookSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
       model = BooksBookSubjects
       fields = '__all__' 



class BooksBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
       model = BooksBookshelf
       fields = '__all__' 


class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
       model =BooksFormat
       fields = '__all__' 

class BooksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
       model =  BooksLanguage
       fields = '__all__' 


class  BooksSubjectSerializer(serializers.ModelSerializer):
    class Meta:
       model =   BooksSubject
       fields = '__all__' 
