from django.db import models
from tools.general.models import SuperClass
from django.utils.translation import ugettext_lazy as _


class Clients(SuperClass):

    company_name = models.CharField(
        _('Empresa'), 
        blank=False, null=False, max_length=50)


    #created_by = models.ForeignKey(
    #    'users.User', verbose_name=_('criado por'),
    #    on_delete=models.DO_NOTHING, related_name='created_by', blank=False, null=True)


class Filial(SuperClass):

    company = models.ForeignKey(
        Clients, verbose_name='Empresa',
        on_delete=models.CASCADE, blank=False, null=False
    )

    filial_name = models.CharField(
        _('Empresa'), 
        blank=False, null=False, max_length=50)

    cnpj = models.CharField(_('CNPJ'), max_length=18)