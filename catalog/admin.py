from django.contrib import admin
from .models import Author, BookInstance, Book, Genre

# Register your models here.
# admin.site.register (Author)
class AuthorAdmin(admin.ModelAdmin):
     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register (Author, AuthorAdmin)

#@admin.register does the same thing as admin.site.register()
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display= ('book', 'status', 'due_back')
    list_filter=('status', 'due_back')
    fieldsets = (
        ("Book Details", {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass



# admin.site.register (BookInstance)
# admin.site.register (Book)
# admin.site.register (Genre)
