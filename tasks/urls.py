from django.urls import path

from . import views
from .views import TasksCreate, TaskDelete, TasksListView, TaskDetail

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_list'),
    path('create/', TasksCreate.as_view(), name='create-tasks'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='delete-tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('index/', views.index),
]
