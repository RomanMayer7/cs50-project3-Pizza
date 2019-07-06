from django.db import models

# Create your models here.
class Extra(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Addition(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    name = models.CharField(max_length=64)
    p_class=models.CharField(max_length=64)
    num_extras=models.IntegerField()
    s_price=models.FloatField()
    l_price=models.FloatField()
    def __str__(self):
        return f"{self.p_class} {self.name}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    have_addons=models.BooleanField()
    s_price=models.FloatField()
    l_price=models.FloatField()
    def __str__(self):
        return f"{self.name} Sub"

class Order(models.Model):
    name = models.CharField(max_length=64)
    o_type= models.CharField(max_length=64)
    size=models.CharField(max_length=64)
    extras=models.CharField(max_length=512)
    price=models.FloatField()
    owner=models.CharField(max_length=64)
    status=models.CharField(max_length=64)
    def __str__(self):
        return f"Order number:{self.id} by {self.owner}"

class Dinner(models.Model):
    name = models.CharField(max_length=64)
    s_price=models.FloatField()
    l_price=models.FloatField()
    def __str__(self):
        return f"{self.name} Dinner Platter"

class Pastasalad(models.Model):
    name = models.CharField(max_length=64)
    p_class= models.CharField(max_length=64)
    price=models.FloatField()
    def __str__(self):
        return f"{self.name}"        