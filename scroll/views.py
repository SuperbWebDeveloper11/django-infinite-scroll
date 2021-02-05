from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .dummy_list import dummy_books

def book_list(request):
    books = dummy_books
    paginator = Paginator(books, 5)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger: 
        books = paginator.page(1) # deliver the first page
    except EmptyPage:
        if request.is_ajax(): # the page is out of range 
            return HttpResponse('') # return an empty page
        books = paginator.page(paginator.num_pages) # range deliver last page 

    if request.is_ajax():
        print('ajax request')
        return render(request, 'scroll/book/list_ajax.html', {'section': 'books', 'books': books})

    return render(request, 'scroll/book/list.html', {'section': 'books', 'books': books})


