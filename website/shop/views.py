from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):

    return  render (request,'shop/index.html')

def about(request):

    return  HttpResponse("about")
def contact(request):

    return  HttpResponse("contact")
def tracker(request):

    return  HttpResponse("tracker")
def  Search( request):

    return  HttpResponse("Search")
def product(request):

    return  HttpResponse("productview")
def checkout(request):

    return  HttpResponse("checkout")



