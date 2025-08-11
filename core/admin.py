from django.contrib import admin

# Register your models here.
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    search_fields = ['title', 'owner__username', ]

    class Meta:
        model = Project