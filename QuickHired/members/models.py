from django.db import models

class Member(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	phone = models.IntegerField(null=True)
	joined_date = models.DateField(null=True)
	note = models.FloatField(null=True)

def __str__(self):
	return f"{self.firstname} {self.lastname}"