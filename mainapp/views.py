import django.contrib.messages
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from . import models
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def index(request):
    names = models.NameModel.objects.all().count()
    return render(request, 'mainapp/index.html', {'names': names})


class CreateData(SuccessMessageMixin, CreateView):
    template_name = 'mainapp/create.html'
    model = models.NameModel
    fields = ['name', 'age']
    success_url = reverse_lazy('mainapp:index')
    success_message = "%(name)s was created successfully"


class ReadData(ListView):
    model = models.NameModel


class UpdateData(SuccessMessageMixin, UpdateView):
    model = models.NameModel
    fields = ['name', 'age']
    success_url = reverse_lazy('mainapp:index')
    success_message = '%(name)s was updated successfully'


class DeleteData(SuccessMessageMixin, DeleteView):
    model = models.NameModel
    success_url = reverse_lazy('mainapp:index')
    success_message = 'Data was deleted successfully'
