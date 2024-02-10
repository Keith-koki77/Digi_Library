from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """
    Represents a category for files in the application.

    Attributes:
        name (str): The name of the category.
    """
    name = models.CharField(max_length=255)

    class Meta:
        """
        Meta class for Category model.

        Attributes:
            ordering (tuple): A tuple specifying the default ordering of categories by name.
            verbose_name_plural (str): A human-readable name for the model in plural form.
        """
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
         Returns a string representation of the Category instance.

        Returns:
            str: A string representation of the category.
        """
        return self.name


class File(models.Model):
	"""
    Represents an file(book) for sale in the application.
    """

	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	publication_year = models.PositiveIntegerField()
	category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
	language = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	available = models.BooleanField(default=True)
	rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
	num_ratings = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='file_images', blank=True, null=True)
	created_by = models.ForeignKey(User, related_name='files', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	file_type = models.CharField(max_length=50, choices=[('pdf', 'PDF'), ('slides', 'Slides')])
	file = models.FileField(upload_to='files/')


	def __str__(self):
		return self.name