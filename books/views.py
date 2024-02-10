from django.shortcuts import render, redirect

from file.models import Category, File

from .forms import SignupForm

from django.contrib.auth import logout

from django.contrib.auth import logout as auth_logout



def index(request):
    """
    This function handles the index page.
    
    :param request: The HTTP request object.
    :return: The rendered index page with categories and items.
    """
    files = File.objects.filter(available=True)[0:6]
    categories = Category.objects.all()

    return render(request, 'books/index.html', {
        'categories': categories,
        'files': files,
    })



def landing(request):
    """
    This function handles the landing page.
    
    :param request: The HTTP request object.
    :return: The rendered landing page.
    """
    return render(request, 'books/landing.html')



def contact(request):
    """
     This function handles the review page.
    
    :param request: The HTTP request object.
    :return: The rendered review page.
    """
    return render(request, 'books/contact.html')


def about(request):
    """
    This function handles the about page.
    
    :param request: The HTTP request object.
    :return: The rendered about page.
    """
    return render(request, 'books/about.html')



def pricing(request):
    """
    This function handles the pricing page.
    
    :param request: The HTTP request object.
    :return: The rendered pricing page.
    """
    return render(request, 'books/pricing.html')



def reviews(request):
    """
     This function handles the review page.
    
    :param request: The HTTP request object.
    :return: The rendered review page.
    """
    return render(request, 'books/reviews.html')



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



def logout(request):
    """
    This function handles the logout page.
    
    :param request: The HTTP request object.
    :return: The rendered logout page.
    """
    return render(request, 'books/logout.html')









