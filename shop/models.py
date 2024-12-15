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

class Cart(models.Model):
	total = models.DecimalField(max_digits = 5, decimal_places = 2)
	stuff = models.ManyToManyField(Stuff)
	quantity = models.IntegerField()

class CartItem(models.Model):
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    stuff_quantity = models.IntegerField(default=0)

# Create your models here.
