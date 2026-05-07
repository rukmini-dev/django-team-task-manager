from django.contrib import admin
from django.urls import path, include
from tasks.views import dashboard
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
    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='login.html'
    ),
),

path(
    'logout/',
    auth_views.LogoutView.as_view(),
),
]