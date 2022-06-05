from django.contrib import admin

from board.models import Task, Status, Term, Description


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'status', ('creator', 'assignee'), 'description')


admin.site.register(Description)
admin.site.register(Status)
admin.site.register(Term)
