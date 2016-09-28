from rest_framework import serializers
from fixture.models import Play_game_slot_details,Improve_game_slot_details

"""
Play Game slot details serializer
"""


class Play_game_slot_details_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Play_game_slot_details
        fields = ('play_fixture_id', 'play_game_day', 'play_game_slot', 'play_game_rating', 'play_session_description')


"""
Improve Game slot details serializer
"""

class Improve_game_slot_details_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Improve_game_slot_details
        fields = ('improve_fixture_id', 'improve_game_day', 'improve_game_slot', 'improve_game_rating', 'improve_session_description')
