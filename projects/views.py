from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .forms import ProjectForm
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm


@login_required
def projects_page(request):

    projects = Project.objects.all()

    return render(
        request,
        'projects/projects.html',
        {'projects': projects}
    )


@login_required
def create_project(request):

    if request.user.role != 'admin':
        return redirect('/')

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)

            project.created_by = request.user

            project.save()

            return redirect('/projects/')

    else:

        form = ProjectForm()

    return render(
        request,
        'projects/create_project.html',
        {'form': form}
    )


@login_required
def delete_project(request, id):

    if request.user.role != 'admin':
        return redirect('/')

    project = get_object_or_404(
        Project,
        id=id
    )

    project.delete()

    return redirect('/projects/')


@login_required
def project_detail(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    tasks = project.task_set.all()

    return render(
        request,
        'projects/project_detail.html',
        {
            'project': project,
            'tasks': tasks
        }
    )