from django.db import models

# Create your models here.


class Product(models.Model):
    item_name = models.CharField(max_length=50,blank=True, null=True)
    rate = models.CharField(max_length=50, blank=True, null = True)
    item_len = models.FloatField(blank=True, null = True )
    item_width = models.FloatField(blank=True, null = True )
    valid_from =  models.DateField(blank = True, null = True )      
    valid_upto =  models.DateField(blank = True, null = True )  
    valid_yn = models.BooleanField(default = True)

