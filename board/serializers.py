from rest_framework import serializers

from board.models import Task, Term, Status, Description


class ListTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ('id', 'name')


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'name')


class DescriptionSerializer(serializers.ModelSerializer):
    terms = ListTermSerializer(many=True, read_only=True)

    class Meta:
        model = Description
        fields = ('description', 'terms')


class TaskSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'creator', 'assignee')

    def create(self, validated_data):
        description_data = validated_data.pop('description')
        description = Description.objects.create(**description_data)
        validated_data['description'] = description
        task = Task.objects.create(**validated_data)

        return task

    def update(self, instance, validated_data):
        description_data = validated_data.pop('description')

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        description = Description.objects.get(pk=instance.description.id)
        description.description = description_data.get('description', description.description)
        description.save()

        return instance


class TermSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()

    class Meta:
        model = Term
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        description_data = validated_data.pop('description')
        description = Description.objects.create(**description_data)
        validated_data['description'] = description
        term = Term.objects.create(**validated_data)

        return term

    def update(self, instance, validated_data):
        description_data = validated_data.pop('description')

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        description = Description.objects.get(pk=instance.description.id)
        description.description = description_data.get('description', description.description)
        description.save()

        return instance
