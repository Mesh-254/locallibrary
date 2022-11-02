from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    """View function for index page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    #Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0) 
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(LoginRequiredMixin, ListView):
    #alternative location to redirect the user to if they are not authenticated (login_url)
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    model = Book
    paginate_by = 4

    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

    def get_queryset(self):
        return Book.objects.all()
        # return Book.objects.filter(title__icontains='Google')


class BookDetailView(DetailView):
    """BookDetailView class provides information about a specific book """
    model = Book


class AuthorListView(LoginRequiredMixin, ListView):
    """AuthorListView class provides information about all authors """
    model = Author
    paginate_by = 4
    context_object_name = 'author_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    
    def get_queryset(self):
        return Author.objects.all()

class AuthorDetailView(DetailView):
    """AuthorDetailView class provides information about a specific author """
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

    

    
    



