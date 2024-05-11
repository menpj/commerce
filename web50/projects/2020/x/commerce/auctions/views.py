from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import User,Listing,Bid
from django.db.models import Max


def index(request):
    
    #highestBid = Bid.objects.values('listingid').annotate(hbid=Max('bid'))
    highestBid = Bid.objects.values('listingid').annotate(hbid=Max('bid'))
    
    #print(testing1)
    #highestBid= Bid.objects.aggregate(Max('bid')) 
    #print(highestBid[0]['hbid'])
    hBid=list(highestBid)  
    #print(type(highestBid))
    highestBid={}
    for bid in hBid:
        highestBid[bid['listingid']]=bid['hbid']

    #for bid in highestBid:
    #   print(bid)
    print(highestBid)
    #print(highestBid['0])
    lisitngs= list(Listing.objects.values())
    #print(lisitngs)
    for listing in lisitngs:
        listing["hbid"]=highestBid[listing["listingid"]]
        #listing["hbid"]=highestBid[1]
    print(lisitngs)
    
    #print(highestBid[4])
    return render(request, "auctions/index.html", {"listings":lisitngs})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    

class NewListingForm(forms.Form):
    title=forms.CharField(label="New Listing Title",empty_value="Title",max_length=100)
    description=forms.CharField(label="Listing Description",widget=forms.Textarea)
    bid=forms.DecimalField(label="Base Bid",min_value=0)
    imageurl=forms.URLField(label="URL of Image",required=False)
    category=forms.CharField(label="Category",required=False)
def createlisting(request):

    if request.method=="POST":
        form=NewListingForm(request.POST)
        if form.is_valid():
            ursid=request.user
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            bid = form.cleaned_data["bid"]
            imageurl = form.cleaned_data["imageurl"]
            category = form.cleaned_data["category"]
            print(title)
            print(description)
            print(bid)
            if imageurl:
                print(imageurl)
            if category:
                print(category)
            listing=Listing(title=title,description=description,basebid=bid,imageurl=imageurl,category=category,usrid=ursid)
            
           
            listing.save()
            print("lisitng:")
            #listing=Listing.objects.get(listing)
            #print(type(listing))
            listingid=listing.listingid
            listing=Listing.objects.get(pk=listingid)

            print(listing)
            bid=Bid(listingid=listing ,bid=bid)
            bid.save()
            print("bid:")
            print(bid)
            
            
            
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"auctions/createlisting.html",{
                "form":form
            })

    return render(request, "auctions/createlisting.html",{"form": NewListingForm()}) 


def listing(request,listing_id):
    print(listing_id)
    
