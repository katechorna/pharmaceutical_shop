from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Product


@login_required
def index(request):
    products = Product.objects.order_by("-id")
    return render(request, "shop/listing.html", {
        "products": products,
        "user": request.user
    })


@login_required
def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "shop/detail.html", {
        "product": product,
        "user": request.user
    })


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "GET":
        return render(request, "shop/sign_in.html")

    params = request.POST
    username = params.get("username")
    password = params.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return render(request, "shop/sign_in.html", {"error": True})
    login(request, user)
    return redirect("index")


def sign_out(request):
    logout(request)
    return redirect("sign_in")
