from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SinupForm, UserForm, ProfileForm
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from core.models import Project


def register(request):
    if request.method == 'POST':
        form = SinupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/account/profile')
            else:
                messages.error(request, 'Error creating user account')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SinupForm()
    
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'account/profile.html', {'profile': profile})

@login_required
def edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()            
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Error updating your profile')       
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
            
    return render(request, 'account/profile_edit.html', {'userform': userform, 'profileform': profileform})


def my_projects(request):
    # logic to show user's projects
    return render(request, 'core/myprojects.html')



# def project_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
    
#     if project.target > 0:
#         progress_percentage = (project.raised / project.target) * 100
#     else:
#         progress_percentage = 0

#     return render(request, 'projects/project_detail.html', {
#         'project': project,
#         'progress_percentage': round(progress_percentage, 2)
#     })
