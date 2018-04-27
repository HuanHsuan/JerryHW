from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=20)
	email_address = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)
	def __str__(self):
		return self.name


class Introduction(models.Model):
	about_myself = models.CharField(max_length=200)
	profile = models.ForeignKey(Profile)
	def __str__(self):
		return self.about_myself


class Hobby(models.Model):
	interest = models.CharField(max_length=20)
	about_hobby = models.CharField(max_length=200)	 
	profile = models.ForeignKey(Profile)
	def __str__(self):
		return self.interest
