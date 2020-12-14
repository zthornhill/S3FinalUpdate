from django.utils import timezone
from django.db import models


# Create your models here.
class Client(models.Model):
    CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    client_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    height = models.IntegerField(blank=False, null=False)
    weight = models.IntegerField(blank=False, null=False)
    account_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.client_name)

class MealTracker(models.Model):
    CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack')
    )
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='mealtrack')
    meal_category = models.CharField(max_length=50, choices= CHOICES)
    meal_description = models.TextField()
    time = models.DateTimeField(
        default=timezone.now)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()
    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.client_name)


