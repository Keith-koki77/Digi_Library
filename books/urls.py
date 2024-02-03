from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'books'

urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.signup, name='signup'),
	path('login/', auth_views.LoginView.as_view(template_name='books/login.html', authentication_form=LoginForm), name='login'),
	path('book/<int:book_id>/borrow/', views.borrow_book, name='borrow_book'),
	path('book/<int:book_id>/return/', views.return_book, name='return_book')
]