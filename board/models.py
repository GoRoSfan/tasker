from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Description(models.Model):
    description = models.TextField(verbose_name=_('Description'))
    terms = models.ManyToManyField('Term', related_name='descriptions', blank=True)

    class Meta:
        verbose_name = _('Description')
        verbose_name_plural = _('Descriptions')

    def __str__(self):
        return self.description[:40]

    def __repr__(self):
        return f'Description({self.pk})'


class Task(models.Model):

    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.ForeignKey(
        Description, models.SET_NULL, null=True, verbose_name=_('Description')
    )
    status = models.ForeignKey(
        'Status', models.SET_NULL, null=True, related_name='tasks', verbose_name=_('Status')
    )
    creator = models.ForeignKey(
        User, models.SET_NULL, null=True, related_name='creator_tasks', verbose_name=_('Creator')
    )
    assignee = models.ForeignKey(
        User, models.SET_NULL, null=True, related_name='assignee_tasks', verbose_name=_('Assignee')
    )

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

    description = models.ForeignKey(
        Description, models.SET_NULL, null=True, verbose_name=_('Description'), related_name='term_description'
    )

    class Meta:
        verbose_name = _('Term')
        verbose_name_plural = _('Terms')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Term({self.name})'
