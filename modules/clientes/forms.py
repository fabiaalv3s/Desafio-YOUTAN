from multiprocessing.connection import Client
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Clients, Filial

class EditCNPJ(forms.Form):
    TYPE_CHOICES = (
        ('ACTIVE', "Ativo"),
        ('INATIVE', "Inativo")
    )

    active = forms.ChoiceField(
        required=False, label=_('choices'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=TYPE_CHOICES)
    cnpj = forms.CharField(
        label="CNPJ", required=True, widget=forms.TextInput(attrs={'class': 'form-control cnpj-mask', }))
    company_name = forms.CharField(
        label="Nome", required=True, widget=forms.TextInput(attrs={'class': 'form-control', }))

class FormClient(forms.ModelForm):

    TYPE_CHOICES = (
        (True, "Sim"),
        (False, "Não")
    )

    active = forms.ChoiceField(
        required=False, label=_('Ativo'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=TYPE_CHOICES)

    company_name = forms.CharField(
        label="Nome", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}))

    class Meta:
        model = Clients
        fields = ['active', 'company_name']

    

class NewFilial(forms.ModelForm):
    TYPE_CHOICES = (
        (True, "Sim"),
        (False, "Não")
    )

    company = forms.ModelChoiceField(
        label='',queryset=Clients.objects.all(), widget=forms.HiddenInput
    )

    active = forms.ChoiceField(
        required=False, label="Ativo",
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=TYPE_CHOICES)

    cnpj = forms.CharField(
        label="CNPJ", required=True, widget=forms.TextInput(attrs={'class': 'form-control cnpj-mask', }))

    filial_name = forms.CharField(
        label="Nome", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}))
    
    class Meta:
        model = Filial
        fields = ['active', 'cnpj', 'filial_name', 'company']
