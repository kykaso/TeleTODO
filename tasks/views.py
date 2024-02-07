from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

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
    success_url = reverse_lazy('taskslist')

    def form_valid(self, form):
        messages.success(self.request, "Успешно удалено")
        return super(TaskDelete, self).form_valid(form)


class TasksCreate(CreateView):
    model = Tasks
    fields = ['title', 'description']
    success_url = reverse_lazy('taskslist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Таск был успешно создан.")
        return super(TasksCreate, self).form_valid(form)
