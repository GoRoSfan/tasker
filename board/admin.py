from django.contrib import admin

from board.models import Task, Status, Term


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'status', ('creator', 'assignee'), 'description', 'terms')


admin.site.register(Status)
admin.site.register(Term)
