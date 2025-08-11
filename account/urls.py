from django.urls import path, include

from .import views



urlpatterns =[
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit/', views.edit, name='profile_edit'),   
    path('myprojects/', views.my_projects, name='myprojects'),
] 
