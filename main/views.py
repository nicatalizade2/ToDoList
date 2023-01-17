from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView

from .forms import TaskCreateForm, RegisterForm
from .models import Task

from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        content = super(TaskList, self).get_context_data(**kwargs)
        content['tasks'] = content['tasks'].filter(user=self.request.user)

        # search = self.request.GET.get('search') or ''
        # if search:
        #     content['tasks'] = content['tasks'].filter(title__icontains=search)
        #
        # content['search'] = search

        return content

    def get_queryset(self):
        query = self.request.GET.get('search') or ''
        querylist = Task.objects.filter(title__icontains=query)
        return querylist



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'tasks'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create.html'
    success_url = reverse_lazy('home')
    context_object_name = 'tasks'
    form_class = TaskCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'update.html'
    success_url = reverse_lazy('home')
    context_object_name = 'tasks'


class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'tasks'


class LoginUser(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            return super(RegisterUser, self).form_valid(form)

