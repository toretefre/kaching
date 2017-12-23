from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    balance = models.CharField(default=0)
    mifare = models.PositiveIntegerField(max_length=200, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    # For use as shopping cart: False until transaction is completed
    checked_out = models.BooleanField(models.BooleanField(default=False))
    # Multiple items should be possible
    # Total amount should be calculated in some way

    def __str__(self):
        return self.id


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    EAN = models.PositiveIntegerField(max_length=13)
    active_item = models.BooleanField(default=True)

    def __str__(self):
        return self.name