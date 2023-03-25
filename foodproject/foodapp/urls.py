
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="foodhome"),
    path("about/",views.about,name="about"),
    path("burgerlist/", views.bugerlist, name="burgerlist"),
    
    path("contact/",views.contact,name="contact"),
    path("search/",views.search,name="search"),
    path("checkoutbill/",views.checkout,name="c"),
    path("success/",views.success,name="s"),
    path("show/",views.show,name="show"),
    path("payment/",views.payment,name="sb"),
    path("register/",views.register,name="regis"),
    path("signin/",views.signin,name="signin"),
    path("signout/",views.signout,name="signout"),
    


]
