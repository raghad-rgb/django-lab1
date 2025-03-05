from django.urls import path
from .views import trainee_list, add_trainee, update_trainee, delete_trainee, register

urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('add/', add_trainee, name='add_trainee'),
    path('update/<int:id>/', update_trainee, name='update_trainee'),
    path('delete/<int:id>/', delete_trainee, name='delete_trainee'),
    path('register/', register, name='register'),
]
