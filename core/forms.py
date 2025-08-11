from django import forms
from  .models import Project, Donation

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_time', 'end_time', 'image']
        

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']