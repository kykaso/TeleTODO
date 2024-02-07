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


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('taskslist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Task'


class TasksCreate(CreateView):
    model = Tasks
    fields = ['title', 'description']
    success_url = reverse_lazy('taskslist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Таск был успешно создан.")
        return super(TasksCreate, self).form_valid(form)
