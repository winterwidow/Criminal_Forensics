from django.db import models

# Create your models here.
class Member(models.Model):
    
    cr_firstname = models.CharField(max_length=255)
    cr_lastname = models.CharField(max_length=255)
    cr_dna = models.CharField(blank=True,max_length=200)
