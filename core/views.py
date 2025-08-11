from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project , Donation
from .forms import ProjectForm , DonationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


# all projects

def home(request):
    return render(request, 'core/home.html')

def all_projects(request):
    
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects})




@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)  
    return render(request, 'core/project_detail.html', {'project': project})

# sepcific projects for user
def my_projects(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'core/myprojects.html', {'projects': projects})


# create project
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, 'Project created successfully')
            return redirect('my_projects')
    else:
        form = ProjectForm()
    return render(request, 'core/create_project.html', {'form': form})


@login_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully')
            return redirect('my_projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'core/edit_project.html', {'form': form})


@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    messages.success(request, 'Project deleted successfully')
    return redirect('my_projects')


# donate
@login_required
def donate(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        donation = Donation(project=project, user=request.user)
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Donation successful')
            return redirect('project_detail', project_id=project_id)
    else:
        form = DonationForm()
    return render(request, 'core/donate.html', {'form': form, 'project': project})