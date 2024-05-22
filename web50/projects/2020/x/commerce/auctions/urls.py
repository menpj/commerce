from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting",views.createlisting,name="createlisting"),
    path("listingpage/<int:listing_id>/",views.listingpage,name="listingpage"),
    path("watchlistpage",views.watchlistpage,name="watchlistpage"),
    path("category",views.category,name="category"),
    path("category/<str:cat_name>",views.category,name="category")
    #path("listingpage/",views.listingpage,name="listingpage"),
    #path("listingpage/",views.listingpage,name="listing"),
    #path("listingpage/<int:listing_id>",views.listingpage,name="listingpage")
]
