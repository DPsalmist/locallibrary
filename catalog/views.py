from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    context_object_name = 'my_book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all()
    #queryset = Book.objects.filter(title__icontains='ea')[:5] # Get 5 books containing the title war
    template_name = 'catalog/book_list.html'

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='ea')[:5]
    

# class BookListView(generic.ListView):
#     model = Book

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(BookListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context 

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 3
	context_object_name = 'author_list'
	queryset = Author.objects.all()
	template_name = 'catalog/author_list.html'

class AuthorDetailView(generic.DetailView):
	"""class to return an author's detail """
	model = Author

	# def get_queryset(self):
	# 	"""Queryset to return all authors in the model """
	# 	return Author.objects.all()
