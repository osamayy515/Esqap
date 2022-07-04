from fnmatch import fnmatchcase
from pyexpat import model
from venv import create
from django.db import models

class Username(models.Model):
    # fname = models.CharField(max_length=50)
    # lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)
    
    # def __str__(self):
    #     return self.fname + ' ' + self.lname