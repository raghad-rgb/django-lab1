from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from course_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainee/', include('trainee_app.urls')),
    path('course/', include('course_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home')
]
