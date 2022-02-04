from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.registeration_page, name = 'register' ),
    path('login/', views.login_user_page, name = 'login'),
    path('logout/', views.logout_user_page, name = 'logout'),
    # path('register/', views.register_page, name = 'register'),
    # path('', views.todo, name = 'home'),
    path('', views.create, name = 'create-task'),
    path('update-task/<str:pk>/', views.updateTask, name = 'update-task'),
    path('delete-task/<str:pk>/', views.deleteTask, name = 'delete-task'),
   
   
]