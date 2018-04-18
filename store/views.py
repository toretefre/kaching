from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.

def storefront(request):
	customers = Customer.objects.all()
	return render(request,'store/accountSelection.html',{'customers':customers})

