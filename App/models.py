from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    brand=models.CharField(max_length=20)
    model=models.CharField(max_length=25)
    color=models.CharField(max_length=25)
    price=models.IntegerField()
    year=models.IntegerField()
    place=models.CharField(max_length=20)
    image=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.model
    
class Spare(models.Model):
    model=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to='gallery')
    type=models.CharField(max_length=20)
    def __str__(self):
        return self.model
    
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle} in {self.user.username}\'s wishlist'
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.spare}'
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name