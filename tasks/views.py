from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from .models import Tasks


# Create your views here.

class TasksListView(ListView):
    model = Tasks
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks_list"


def index(request):
    return render(request, 'tasks/index.html')


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        messages.success(self.request, "Успешно удалено")
        return super(TaskDelete, self).form_valid(form)


class TasksCreate(CreateView):
    model = Tasks
    fields = ['title', 'description']
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Таск был успешно создан.")
        return super(TasksCreate, self).form_valid(form)


class TaskDetail(DetailView):
    model = Tasks
    context_object_name = 'task'