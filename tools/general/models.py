from django.db import models
from django.utils.translation import ugettext_lazy as _


class SuperClass(models.Model):
    class Meta:
        abstract = True
        ordering = ('-created_at',)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    deleted_at = models.DateTimeField(_('deleted at'), null=True, blank=True)
    active = models.BooleanField(_('active'), default=True)