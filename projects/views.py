from django.shortcuts import render

# Create your views here.
# projects/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

# read (List)
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})

# create
def project_create(request):
    if request.method == 'POST':
        # MUST pass both request.POST and request.FILES
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'projects/project_form.html', {
        'form': form,
        'action': 'Create'
    })

# update
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        # Pass instance=project to update the existing record
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_form.html', {
        'form': form,
        'action': 'Edit',
        'project': project
    })

# delete
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        # Optional: delete the physical file from storage when deleting the record
        if project.proposal_file:
            project.proposal_file.delete(save=False)
        project.delete()
        messages.success(request, 'Project deleted.')
        return redirect('project_list')

    return render(request, 'projects/project_confirm_delete.html', {'project': project})