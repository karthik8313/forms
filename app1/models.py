from django.db import models

class blogform3(models.Model):
	First_Name=models.CharField(max_length=20,blank=True)
	Last_Name=models.CharField(max_length=20,blank=True)
	Middle_Name=models.CharField(max_length=20,blank=True)