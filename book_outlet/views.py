from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):

    books = Book.objects.all().order_by()
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request,"book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": num_books
        })

def book_detail(request, slug):


    book = get_object_or_404(Book, slug=slug)

  
    return render(request, "book_outlet/book-detail.html",{
       "book": book
    })
    

