from django.http import HttpResponse
from .models import Book
from django.views.generic import TemplateView
from .utils import average_rating
from django.shortcuts import render


def home_page(request):
    return render(request, 'reviews/base.html')

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0

        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
        
    context = {
        'book_list': book_list
    }

    return render(request, 'reviews/book_list.html', context = context)


