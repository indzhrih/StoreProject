from django.db import models
from django.urls import reverse

class Stuff(models.Model):
	title = models.CharField(max_length = 255)
	body = models.TextField()
	image = models.ImageField(upload_to = "media/")
	price = models.DecimalField(max_digits = 5, decimal_places = 2)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('stuff_list')

# Create your models here.
