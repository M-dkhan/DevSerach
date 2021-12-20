from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects,
    }
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    context = {
        'project':projectObj,
    }
    return render(request, 'projects/single-project.html',context)



def createProject(request):
    projectForm = ProjectForm()
    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES)
        if projectForm.is_valid():
            projectForm.save()
            return redirect('projects')

    context = {
        'form':projectForm,
    }
    return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
    projectObj = Project.objects.get(id=pk)
    projectForm = ProjectForm(instance= projectObj)

    if request.method == 'POST':
        projectForm = ProjectForm(request.POST, request.FILES,instance=projectObj)
        if projectForm.is_valid():
            projectForm.save()
            return redirect('projects')

    context = {
        'form':projectForm,
    }
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    projectObj = Project.objects.get(id=pk)
    if request.method == 'POST':
            projectObj.delete()
            return redirect('projects')

    context = {
        'project':projectObj,
    }
    return render(request, 'projects/delete_template.html', context)
