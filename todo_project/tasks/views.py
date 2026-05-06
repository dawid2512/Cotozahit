from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Song
from .serializers import SongSnippetSerializer


def home(request):
    return render(request, 'home.html')


class RandomSongView(APIView):
    def get(self, request):
        song = Song.objects.order_by('?').first()
        if not song:
            return Response({"error": "Brak piosenek w bazie"}, status=404)
        serializer = SongSnippetSerializer(song)
        return Response(serializer.data)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Song

class CheckAnswerView(APIView):
    def post(self, request):
        song_id = request.data.get('id')
        user_answer = request.data.get('answer', '').strip().lower()
        
        try:
            song = Song.objects.get(id=song_id)
            is_correct = song.title.lower() == user_answer
            
            if is_correct:
                return Response({'is_correct': True})
            else:
                return Response({
                    'is_correct': False,
                    'second_snippet': song.second_snippet,
                    'artist': song.artist,
                    'correct_title': song.title
                })
        except Song.DoesNotExist:
            return Response({'error': 'Nie znaleziono piosenki'}, status=404)