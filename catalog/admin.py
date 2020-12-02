from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class AuthorInstanceInline(admin.TabularInline):
	model = Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	#fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	inlines = [AuthorInstanceInline]
	fieldsets = (
		('About Author', {
			'fields':('first_name', 'last_name', 'date_of_birth', 'date_of_death')
			}),
		)

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#for inline or tabular display
class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]



# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back') 
	#book, status, due back date, and id
	list_display = ('book','status','due_back', 'id')
	fieldsets = (
        ('Book Det.', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )