# import the auth module for datestamp creation by admin/user

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User=get_user_model()


class FooModel(models.Model):
    country_name = models.CharField(max_length=30)
    country_size = models.CharField(max_length=30)
    presidents_name = models.CharField(max_length=20)
    datestamp = models.DateTimeField(auto_now_add=True)
    ethnicity = models.CharField(max_length=30, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.country_name