from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

#Defirnir la clase admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

#Registrar la clase admin con el modelo asociado
admin.site.register(Author,AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
#Registar la clase admin para Book con un decorador
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','display_genre')
    inlines = [BooksInstanceInline]

#Registrar la clase admin para BookInstance con un decorador
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back','id')
    #list_display = ('display_book','status','due_back','id')
    list_filter = ('status','due_back')
    fieldsets = ((None,{'fields': ('book', 'imprint', 'id')}),
    ('Availability',{'fields': ('status', 'due_back', 'borrower')}))

