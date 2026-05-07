from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from projects.models import Project
from users.models import User


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def dashboard(request):

    if request.user.is_authenticated and request.user.role == 'admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=request.user)

    if request.method == 'POST' and request.user.is_authenticated and request.user.role == 'admin':
        form_type = request.POST.get('form_type')

        if form_type == 'project':

            Project.objects.create(
                title=request.POST.get('project_title'),
                description=request.POST.get('project_description'),
                created_by=request.user
            )

        elif form_type == 'task':

            Task.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                status='todo',
                due_date=request.POST.get('due_date'),
                assigned_to=User.objects.get(
                    id=request.POST.get('assigned_to')
                ),
                project=Project.objects.get(
                    id=request.POST.get('project_id')
                )
            )

        return redirect('/')

    context = {
        'tasks': tasks,
        'total': tasks.count(),
        'completed': tasks.filter(status='done').count(),
        'pending': tasks.exclude(status='done').count(),
        'overdue': tasks.filter(due_date__lt=now().date()).count(),
        'users': User.objects.filter(role='member'),
        'projects': Project.objects.all()
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )


@login_required
def projects_page(request):

    projects = Project.objects.all()

    return render(
        request,
        'projects/projects.html',
        {'projects': projects}
    )


@login_required
def project_detail(request, id):

    project = Project.objects.get(id=id)

    tasks = Task.objects.filter(project=project)

    return render(
        request,
        'projects/project_detail.html',
        {
            'project': project,
            'tasks': tasks
        }
    )


@login_required
def tasks_page(request):

    tasks = Task.objects.all()

    return render(
        request,
        'tasks/tasks.html',
        {'tasks': tasks}
    )


@login_required
def members_page(request):

    users = User.objects.all()

    return render(
        request,
        'members/members.html',
        {'users': users}
    )