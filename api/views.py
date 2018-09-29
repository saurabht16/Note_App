from django.shortcuts import render
# Create your views here.

from rest_framework import generics

from notes import models
from . import serializers


class ListNotes(generics.ListCreateAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer


class DetailNotes(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer

class LabelSearch(generics.ListAPIView):
    serializer_class = serializers.NotesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the notes for
        the labels in teh labels portion of the URL.
        """
        labels = self.kwargs['labels']
        return models.Notes.objects.filter(labels__icontains=labels)