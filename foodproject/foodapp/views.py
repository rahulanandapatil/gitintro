from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product, Contact, Burger, Order
from django.core.mail import send_mail
# Create your views here.


def index(request):
    prod = Product.objects.all()
    return render(request, "foodapp/index.html", {'prod': prod})


def about(request):
    return render(request, "foodapp/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        food = request.POST.get('food', '')
        message = request.POST.get('message', '')
        con = Contact(name=name, email=email, food=food, message=message)
        con.save()

        send_mail(
            'New message from ' + name,
            message,
            email,
            ['rahulpatil3830@gmail.com'],
            fail_silently=False
        )
    return render(request, "foodapp/contact.html")


def checkout(request):

    if request.method == "POST":
        f_name = request.POST.get('f_name', '')
        l_name = request.POST.get('l_name', '')
        email = request.POST.get('email', '')
        at = request.POST.get('at', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        pay = request.POST.get('pay', '')

        order = Order(f_name=f_name, l_name=l_name, email=email,
                      at=at, address=address, city=city, pay=pay)
        order.save()

        return render(request, "foodapp/about.html")

    return render(request, "foodapp/checkout.html")


def bugerlist(request):
    burger = Burger.objects.all()
    
    return render(request, "foodapp/burgerlist.html", {'burger': burger})

def search(request):
    query = request.GET['query']
    burger = Burger.objects.filter(bur_name__icontains=query.lower())
    params = {'burger':burger,'query':query}
    return render(request,"foodapp/search.html", params)

def register(request):
    if request.method == 'POST':
        UserName = request.POST['UserName']
        FullName = request.POST['FullName']
        Email = request.POST['Email']
        Password = request.POST['Password']

        myuser = User.objects.create_user(UserName, Email, Password)
        myuser.fullname = FullName
        myuser.save()
        return redirect('/shop')

    else:
        return render(request, "foodapp/signup.html")


def signin(request):
    if request.method == "POST":
        sUserName = request.POST['sUserName']
        sPassword = request.POST['sPassword']

        user = authenticate(username=sUserName, password=sPassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully login")
            return redirect('/shop')
        else:
            messages.error(request, "Invalid Username/Password")
            return redirect('signin')

    else:
        return render(request, "foodapp/signin.html")


def signout(request):
    logout(request)
    return redirect('/shop')

    return HttpResponse('ggg')
