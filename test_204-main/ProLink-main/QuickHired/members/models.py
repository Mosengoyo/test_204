from django.db import models

class Member(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	phone = models.IntegerField(null=True)
	joined_date = models.DateField(null=True)
	note = models.FloatField(null=True)
	def __str__(self):
		return f"{self.firstname} {self.lastname}"

class Product(models.Model):
	name = models.TextField()
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to='products/')
	def __str__(self):
		return f"{self.name} {self.description}"

class Panier(models.Model):
	user = models.TextField()
	product = models.TextField() # models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	total_price = models.DecimalField(max_digits=6, decimal_places=2)
	def __str__(self):
		return f"{self.user} {self.product}"

