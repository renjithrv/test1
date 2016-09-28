from django.shortcuts import render

# Create your views here.

from fixture.serializers import Play_game_slot_details_Serializer,Improve_game_slot_details_Serializer
from fixture.models import Play_game_slot_details,Improve_game_slot_details

from rest_framework import serializers, viewsets, status


from rest_framework.decorators import api_view
from rest_framework.response import Response



 
@api_view(['GET', 'POST'])
def PlaygameslotViewSet(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        playserialize = Play_game_slot_details.objects.all()
        serializer = Play_game_slot_details_Serializer(playserialize, many=True)
        return Response(serializer.data)




        # ViewSets define the view behavior.
class ImprovegameslotViewSet(viewsets.ModelViewSet):
    queryset = Improve_game_slot_details.objects.all()
    serializer_class = Improve_game_slot_details_Serializer



