from django.contrib import admin

from .models import Client, MealTracker


class ClientList(admin.ModelAdmin):
    list_display = ('client_name', 'height', 'weight', 'account_number', 'phone_number')
    list_filter = ('client_name', 'account_number')
    search_fields = ('client_name',)
    ordering = ['client_name']


class MealTrackerList(admin.ModelAdmin):
    list_display = ('client_name', 'meal_category', 'calories', 'time')
    list_filter = ('client_name', 'calories', 'time')
    search_fields = ('client_name',)
    ordering = ['client_name']


admin.site.register(Client)
admin.site.register(MealTracker, MealTrackerList)
