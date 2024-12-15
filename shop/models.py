from django.db import models
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

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
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
	stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} x {self.stuff.title}"

	def total_price(self):
		return self.quantity * self.stuff.price

# Create your models here.
