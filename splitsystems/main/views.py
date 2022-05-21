from django.shortcuts import render
from .models import Condicioneri
from .models import ShoppingCart
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    conds = Condicioneri.objects.all()
    return render(request, 'main/index.html', {'naimenovanie': conds})


def loginPage(request):
    return render(request, 'main/login.html')

def reg(request):
    return render(request, 'main/reg.html')


def regNewUser(request):
    username = request.POST["username"]
    fName = request.POST["fName"]
    lName = request.POST["lName"]
    email = request.POST["email"]
    password = request.POST["password"]
    user = User.objects.create_user(username, email, password)
    return redirect('/login')

def loginUser(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse("Неверный логин или пароль!")

def logoutUser(request):
    logout(request)
    return redirect('/')


def addToShopingCart(request):
    product_id = request.GET['product_id']
    if request.user.is_authenticated:
        new_item = ShoppingCart.objects.create(user=request.user, product_id = product_id)
        request.user.shoppingcart_set.add(new_item)
        return redirect('/')
    else:
        return redirect('../login/')


def ordering(request):
    items = request.user.shoppingcart_set.all()
    products = []
    for item in items:
        product = Condicioneri.objects.get(seriyni_nomer=item.product_id)
        products.append(product)
    return render(request, 'main/ordering.html', {'products': products})







