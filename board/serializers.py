from rest_framework import serializers

from board.models import Task, Term


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'creator', 'assignee', 'terms']


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['name', 'description', 'explanatory_terms']
