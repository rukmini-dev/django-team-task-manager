from django.contrib import admin
from django.urls import path, include
from tasks.views import dashboard
from users.views import register_view
from tasks.views import create_task
from users.views import register_view, create_user,delete_user
from projects.views import create_project,delete_project
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from tasks.views import (
    dashboard,
    projects_page,
    project_detail,
    tasks_page,
    delete_task,
    members_page
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('tasks.urls')),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('', dashboard),

    path('projects/', projects_page),

    path('projects/<int:id>/', project_detail),

    path('tasks-page/', tasks_page),

    path('members/', members_page),
    path('register/', register_view),
    path('register/', register_view),
    path('create-user/', create_user),
    path('create-project/', create_project),
    path(
    'create-task/',
    create_task
    ),
    path(
    'delete-project/<int:id>/',
    delete_project
),
path(
    'delete-user/<int:id>/',
    delete_user
),
path(
    'delete-task/<int:id>/',
    delete_task
),
    path(
    'logout/',
    auth_views.LogoutView.as_view(next_page='/login/'),
    name='logout'
    ),
    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='login.html'
    ),
),

]