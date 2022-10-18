from codecs import unicode_escape_decode
from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    """ Model representing book genres."""
    name = models.CharField(
        max_length=255, help_text="Enter a book genre name.eg.Fiction")

    # metadata
    class Meta:
        """"metadata ordering"""
        ordering = ['name']

    # def get_absolute_url(self):
    #     """ Return the URL to access a particular instance of the model"""
    #     return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self) -> str:
        """ Model object string representation"""
        return self.name


class Book(models.Model):
    """ Model representing a single book. """
    title = models.CharField(max_length=255)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text="Enter brief summary of the book.")
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(
        Genre, help_text='Select a genre for this book.')
    Language = models.CharField(max_length=255, blank=True, help_text='Language for this book')

    def __str__(self):
        """"String representation of genre models"""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])  # type: ignore

    def display_genre(self):
        """Returns a string from the first three values of the genre field
           This is required to display genre in Admin 
        """
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'  # type: ignore


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])  # type: ignore

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
