from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	publication_year = models.PositiveIntegerField()
	isbn = models.CharField(max_length=13)
	language = models.CharField(max_length=50)
	description = models.TextField()
	cover_image = models.ImageField(upload_to='book_covers/')
	available = models.BooleanField(default=True)
	rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
	num_ratings = models.IntegerField(default=0)
	tags = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.title 


class BorrowHistory(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	borrower = models.ForeignKey(User, on_delete=models.CASCADE)
	borrow_date = models.DateField(auto_now_add=True)
	return_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return f"{self.book.title} - {self.borrower.username}"