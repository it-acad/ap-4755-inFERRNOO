from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from .models import Book
from django.contrib.auth import get_user_model
from author.models import Author

User = get_user_model()

def book_list(request):
    books = Book.get_all()
    name = request.GET.get('name')
    author = request.GET.get('author')
    
    if name:
        books = books.filter(name__icontains=name)
    if author:
        books = books.filter(authors__name__icontains=author)
        
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.get_by_id(pk)
    if not book:
        raise Http404("Книгу не знайдено")
    return render(request, 'book_detail.html', {'book': book})

@user_passes_test(lambda u: u.is_staff)
def user_books(request, user_id):
    target_user = get_object_or_404(User, pk=user_id)
    books = Book.objects.filter(borrower=target_user)
    return render(request, 'user_books.html', {'target_user': target_user, 'books': books})

def create_book(request):
    authors = Author.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        count = request.POST.get('count', 10)
        
        author_ids = request.POST.getlist('authors')
        
        Book.create(name=name, description=description, count=count, authors=author_ids)
        
        return redirect('book-list')
        
    return render(request, 'create_book.html', {'authors': authors})