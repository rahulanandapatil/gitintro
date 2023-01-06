from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    product_date = models.DateField()

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    mess_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    food = models.CharField(max_length=200)
    message = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Burger(models.Model):
    bur_id = models.AutoField(primary_key=True)
    bur_name = models.CharField(max_length=50)
    bur_desc = models.CharField(max_length=500)
    bur_price = models.IntegerField(default="")
    def __str__(self):
        return self.bur_name

class Price(models.Model):
    price = models.IntegerField()

    def __str__(self):
        return self.price

class Order(models.Model):
    o_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    pay = models.CharField(max_length=50)
    at = models.IntegerField(default=0)

    def __str__(self):
        return self.f_name



