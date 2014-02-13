from django.db import models
from django.utils.translation import ugettext as _


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first_name'))
    middle_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    last_name = models.CharField(max_length=100, verbose_name=_('middle_name'))

    class Meta(object):
        app_label = 'sample'
        verbose_name_plural = _('people')
