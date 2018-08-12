from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.


def itemSelection(request):
    item = Item.objects.all()
    return render(
        request,
        'itemSelection.html',
        {'items': item}
    )


def customerSelection(request):
    customer = Customer.objects.all()
    return render(
        request,
        'customerSelection.html',
        {'customers': customer}
    )


def finishOrder(request):
    selectedCustomer = 0 # request.customer?
    selectedCustomer.balance = 0 # should be fetched from model
    selectedItems = []
    basketvalue = 0

    for selectedItem in selectedItems:
        basketvalue += selectedItem.value

    if basketvalue < selectedCustomer.balance:
        selectedCustomer.balance -= basketvalue