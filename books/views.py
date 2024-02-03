from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Book, BorrowHistory
from .forms import SignupForm

@login_required
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books
    })

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {
        'book': book
    })

@login_required
def borrow_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        BorrowHistory.objects.create(book=book, borrower=request.user)
        book.available = False
        book.save()
        return redirect('index')
    else:
        return redirect('index')  # Redirect if accessed via GET or other methods

@login_required
def return_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        borrow_history = get_object_or_404(BorrowHistory, book=book, borrower=request.user, return_date=None)
        borrow_history.return_date = timezone.now().date()
        borrow_history.save()
        book.available = True
        book.save()
        return redirect('index')
    else:
        return redirect('index')  # Redirect if accessed via GET or other methods


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    else:
        form = SignupForm()

    return render(request, 'books/signup.html', {
        'form': form
    })
