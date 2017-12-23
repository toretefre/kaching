from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    mail = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)
    mifare = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Item(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    EAN = models.PositiveIntegerField()
    active_item = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
    )

    # Connects with multiple items
    items = models.ManyToManyField(Item)

    # For use as shopping cart: False until transaction is completed
    checked_out = models.BooleanField(models.BooleanField(default=False))

    def __str__(self):
        return self.id
