from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Drink)
admin.site.register(Food)
