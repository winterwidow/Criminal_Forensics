from django.db import models

# Create your models here.
class Member(models.Model):
    
    cr_firstname = models.CharField(null=True,max_length=255,db_index=True)
    cr_lastname = models.CharField(null=True,max_length=255,db_index=True)
    #cr_dna = models.CharField(blank=True,max_length=200)
    cr_gender = models.CharField(null=True,max_length=255,db_index=True)
    cr_crime = models.CharField(null=True,max_length=255,db_index=True)
    cr_weapon = models.CharField(null=True,max_length=255,db_index=True)
    cr_date = models.DateField(null=True,db_index=True)
