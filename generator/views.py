import random
from django.shortcuts import render


def home(request):
    return render(request, "generator/home.html")


def about(request):
    return render(request, "generator/about.html")


def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("specials"):
        characters.extend(list("!@#$%^&*()"))

    length = int(request.GET.get("length", 8))
    the_password = ""
    for element in range(length):
        the_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": the_password})
