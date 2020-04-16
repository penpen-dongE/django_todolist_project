from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home_view(request):
    return render(request, "index.html", {})


def var_view(request):
    present = 10
    return render(request, "var.html", {"students": present})


def nums_view(request):
    nums = [1, 2, 3, 4, 5]
    return render(request, "nums.html", {"students": nums})


def quote_view(request):
    return render(request, "quote.html", {})
