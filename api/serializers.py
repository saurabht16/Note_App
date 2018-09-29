from rest_framework import serializers
from notes import models


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'labels',
            'created_by',
        )
        model = models.Notes