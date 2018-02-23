from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.

def storefront(request):
    print(Customer.objects.all())
    return HttpResponse("Storefront here")

