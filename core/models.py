from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone  


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    details = models.TextField()
    total_target = models.DecimalField(max_digits=12, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='project_pictures/')
    
    
    def clean(self):
        now = timezone.now()
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after the start time.")

        
    def __str__(self):
        return self.title
    
    def total_donated(self):
        return sum(d.amount for d in self.donations.all())

    def remaining_target(self):
        return self.total_target - self.total_donated()
    
    
    @property
    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time
    
    
class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Donation amount must be greater than zero.")
        if self.amount > self.project.remaining_target():
            raise ValidationError("Donation exceeds the remaining target.")

    def __str__(self):
        return f"{self.user.username} donated {self.amount} EGP to {self.project.title}"

    