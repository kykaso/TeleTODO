from django.urls import path

from . import views
from .views import TasksCreate, TaskDeleteView

urlpatterns = [
    path('', views.TasksListView.as_view(), name='taskslist'),
    path('create/', TasksCreate.as_view(), name='create-tasks'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('index/', views.index),
]
