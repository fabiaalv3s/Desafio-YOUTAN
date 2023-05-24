from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from ..clientes.models import Clients
from django.views.generic.list import ListView
from django.views.generic import TemplateView, ListView, DetailView, View, RedirectView, FormView
from ..clientes.forms import FormClient, NewFilial
from django.views.generic.edit import UpdateView, FormView, CreateView, DeleteView

class Home(ListView):
    template_name = "home.html"
    model = Clients
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormClient()

        return context

class CreateClient(CreateView):
    model = Clients
    template_name = 'home.html'
    form_class = FormClient
    success_url = reverse_lazy('home:index')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class UpdateClient(UpdateView):
    model = Clients
    template_name = 'clients.html'
    form_class = FormClient
    success_url = reverse_lazy('home:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newfilial'] = NewFilial(initial={'company': self.kwargs['pk']})
        context['company_pk'] = self.kwargs['pk']
        return context

class DeleteClient(DeleteView):
    model = Clients
    template_name = 'delete.html'
    success_url = reverse_lazy('home:index')
