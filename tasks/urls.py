from django.urls import path

from . import views
from .views import TasksCreate, TaskDelete, TasksListView

urlpatterns = [
    path('', TasksListView.as_view(), name='taskslist'),
    path('create/', TasksCreate.as_view(), name='create-tasks'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='delete-tasks'),
    path('index/', views.index),
]
