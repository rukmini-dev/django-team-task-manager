from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import RegisterForm, CreateUserForm
from .models import User

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.role = 'member'

            user.save()

            login(request, user)

            return redirect('/')

    else:

        form = RegisterForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )


@login_required
def create_user(request):

    if request.user.role != 'admin':
        return redirect('/')

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            return redirect('/members/')

    else:

        form = CreateUserForm()

    return render(
        request,
        'users/create_user.html',
        {'form': form}
    )


@login_required
def delete_user(request, id):

    if request.user.role != 'admin':
        return redirect('/')

    user = get_object_or_404(
        User,
        id=id
    )

    if request.user.id == user.id:
        return redirect('/members/')

    user.delete()

    return redirect('/members/')