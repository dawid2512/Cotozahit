from rest_framework import serializers
from .models import Song

class SongSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'snippet', 'second_snippet']