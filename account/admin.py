from django.contrib import admin
from .models import Profile, City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    
    
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone_number', 'image']
    search_fields = ('user__username', 'user__email','phone_number' )
    list_filter = ('city',)
    
    
