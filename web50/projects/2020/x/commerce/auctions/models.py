from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class Listing(models.Model):
    listingid= models.AutoField(primary_key=True)
    usrid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userlisting")
    title=models.CharField(max_length=100)
    description=models.TextField()
  
    basebid=models.DecimalField(decimal_places=2,max_digits=60)
    category=models.CharField(blank=True,max_length=100)
    imageurl=models.URLField(blank=True)

    def __str__(self):
        return f"user id {self.usrid} created {self.listingid} with {self.title} with {self.description} with base bid {self.basebid}"
    

class Bid(models.Model):
    bidid=models.AutoField(primary_key=True)
    listingid=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="listingbid")
    bid=models.DecimalField(decimal_places=2,max_digits=60)

    def __str__(self):
        #return f"listing id {self.listingid} bid value {self.bid}"
        return f"{self.listingid}"