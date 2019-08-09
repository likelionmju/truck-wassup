from django.db import models

# Create your models here.
class FoodTruck(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Menu(models.Model):
    foodtruck = models.OneToOneField(FoodTruck, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name
