from django import forms
from .models import Client, MealTracker


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'email', 'height', 'weight', 'account_number', 'address',
                  'city', 'state', 'zipcode', 'phone_number')


class MealTrackerForm(forms.ModelForm):
    class Meta:
        model = MealTracker
        fields = ('client_name', 'meal_category', 'meal_description', 'time', 'calories')
