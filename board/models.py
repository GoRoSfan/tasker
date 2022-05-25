from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):

    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    status = models.ForeignKey(
        'Status', models.SET_NULL, null=True, related_name='tasks', verbose_name=_('Status')
    )
    creator = models.ForeignKey(
        User, models.SET_NULL, null=True, related_name='creator_tasks', verbose_name=_('Creator')
    )
    assignee = models.ForeignKey(
        User, models.SET_NULL, null=True, related_name='assignee_tasks', verbose_name=_('Assignee')
    )
    terms = models.ManyToManyField('Term', related_name='tasks', blank=True)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return f'{self.title} ({self.creator})'

    def __repr__(self):
        return f'Task({self.title}, {self.status}, {self.creator}, {self.assignee})'


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Status({self.name})'


class Term(models.Model):

    name = models.CharField(max_length=100, verbose_name=_('Name'))

    description = models.TextField(verbose_name=_('Description'))
    explanatory_terms = models.ManyToManyField('Term', related_name='explicable_terms', blank=True)

    class Meta:
        verbose_name = _('Term')
        verbose_name_plural = _('Terms')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Term({self.name})'
