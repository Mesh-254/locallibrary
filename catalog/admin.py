from django.contrib import admin
from .models import Author, BookInstance, Book, Genre

# Register your models here.
admin.site.register (Author)
admin.site.register (BookInstance)
admin.site.register (Book)
admin.site.register (Genre)
