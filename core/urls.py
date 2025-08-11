from django.urls import path, include

from .import views



urlpatterns =[
  path('', views.home, name='home'),
  path('projects/', views.all_projects, name='all_projects'),
  path('my_projects/', views.my_projects, name='my_projects'),
  path('create_project/', views.create_project, name='create_project'),
  path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
  path('donate/<int:project_id>/', views.donate, name='donate'),
  path('delete_project/<int:id>/delete/', views.delete_project, name='delete_project'),
  path('edit_project/<int:id>/edit/', views.edit_project, name='edit_project'),
] 
