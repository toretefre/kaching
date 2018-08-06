from django.db import models

# Create your models here.


class Customer(models.Model):
    username = models.CharField(primary_key=True, unique=True, max_length=15)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    balance = models.PositiveIntegerField(default=1)
    mifare = models.CharField(blank=True, max_length=14)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Item(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    EAN = models.IntegerField(null=True, blank=True)
    active_item = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Food(Item):
    grams = models.PositiveIntegerField()


class Drink(Item):
    milliliters = models.PositiveIntegerField()


class Order(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    customerForOrder = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True
    )

    # Connects with multiple items
    items = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
        null=True
    )

    # For use as shopping cart: False until order is completed
    checked_out = models.BooleanField(models.BooleanField(default=False))

    def __str__(self):
        return self.id
