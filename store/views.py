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
