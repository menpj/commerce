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
    closed=models.BooleanField(default=False)

    def __str__(self):
        return f"user id {self.usrid} created {self.listingid} with {self.title} with {self.description} with base bid {self.basebid} closed status of lisitng is {self.closed}"
    

class Bid(models.Model):
    bidid=models.AutoField(primary_key=True)
    listingid=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="listingbid")
    bid=models.DecimalField(decimal_places=2,max_digits=60)
    userid= models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name="userbid")
    

    def __str__(self):
        #return f"listing id {self.listingid} bid value {self.bid}"
        return f"{self.listingid}"
    

class Watchlist(models.Model):
    watchlistid= models.AutoField(primary_key=True)
    userid= models.ForeignKey(User,on_delete=models.CASCADE,related_name="userwatchlist")
    listingid = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="listingwatchlist")
    
    class Meta:
        unique_together = ('userid', 'listingid')

    def __str__(self):
        return f"{self.watchlistid} created by {self.userid} with lisitng {self.listingid}"
    
class Comments(models.Model):
    commentid=models.AutoField(primary_key=True)
    userid= models.ForeignKey(User,on_delete=models.CASCADE,related_name="userwatchlistcmnt")
    listingid = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="listingwatchlistcmnt")
    comment=models.TextField()
