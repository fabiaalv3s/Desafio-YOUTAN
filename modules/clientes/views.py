from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from ..clientes.models import Clients, Filial
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.db.models import Q
from .forms import FormClient, NewFilial
from django.http import JsonResponse


class ListClients(FormView):
    template_name = "clients.html"
    form_class = FormClient


class AddClient(View):
    def  get(self, request):
        company_name1 = request.GET.get('company_name', None)
        active1 = request.GET.get('active', None)

        obj = Clients.objects.create(
            active = active1,
            company_name = company_name1,
        )
        
        context = Clients.objects.values()

        print(context)

        data = {
            'context': context
        }
        return JsonResponse(data)


class AjaxFormMixin:

    def form_invalid(self, form):
        return JsonResponse(form.errors.as_data())

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({
            'status': True,
            "pk": self.object.pk,
        })

class AddFilial(AjaxFormMixin, CreateView):
    model = Filial
    form_class = NewFilial


class ListFilial(View):

    def get(self, request):
        query = Q()
        if request.GET.get('company', None):
            query.add(Q(company=request.GET['company']), Q.AND)
        data = Filial.objects.filter(query).values(
            'id','cnpj', 'filial_name', 'active').order_by('created_at')
        return JsonResponse(list(data), safe=False)

class UpdateFilial(View):

    def post(self, request):
        id1 = request.POST.get('filial', None)
        #f = Filial.objects.get(id=id1)
        f = get_object_or_404(Filial, id=id1)
        filialname1 = request.POST.get('filial_name', None)
        active1 = request.POST.get('active', None)
        cnpj1 = request.POST.get('cnpj', None)
        f.active = active1
        f.filial_name = filialname1
        f.cnpj = cnpj1

        f.save()

        data = {
            'update': True
        }
        return JsonResponse(data)
