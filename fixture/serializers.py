from rest_framework import serializers
from fixture.models import Play_game_slot_details,Improve_game_slot_details

"""
Play Game slot details serializer
"""


class Play_game_slot_details_Serializer(serializers.Serializer):
   
    play_fixture_id = serializers.IntegerField(required=True)
    play_game_day = serializers.CharField(required=True, max_length=255)
    play_venue_id = serializers.IntegerField(required=True)
    play_game_slot = serializers.CharField( required=True, allow_blank=False, max_length=100)
    play_court_name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    play_game_max_players = serializers.IntegerField(required=True)
    play_home_batch_takein = serializers.IntegerField(required=True)
    play_home_batch_start_time = serializers.CharField(required=True, max_length=10)
    play_flexi_batch_start_time = serializers.CharField(required=True, max_length=10)
    play_general_cut_off = serializers.CharField(required=True, allow_blank=False, max_length=10)
    play_game_version = serializers.CharField(required=True, allow_blank=False, max_length=5)
    play_game_rating = serializers.CharField(required=True, allow_blank=False, max_length=15)
    play_enable_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_fixture_reminder_sent = serializers.CharField(allow_blank=True, max_length=255)
    play_flexi_fixture_reminder_sent = serializers.CharField(allow_blank=True, max_length=255)
    play_assigned_buddy1 = serializers.IntegerField()
    play_assigned_buddy2 = serializers.IntegerField()
    play_temp_buddy1 = serializers.IntegerField()
    play_temp_buddy2 = serializers.IntegerField()
    play_session_description = serializers.CharField(required=True, allow_blank=False, max_length=255)
 


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Play_game_slot_details.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.play_fixture_id = validated_data.get('play_fixture_id', instance.play_fixture_id)
        instance.play_game_day = validated_data.get('play_game_day', instance.play_game_day)
        instance.play_venue_id = validated_data.get('play_venue_id', instance.play_venue_id)
        instance.play_game_slot = validated_data.get('play_game_slot', instance.play_game_slot)
        instance.play_court_name = validated_data.get('play_court_name', instance.play_court_name)
        instance.play_game_max_players = validated_data.get('play_game_max_players', instance.play_game_max_players)
        instance.play_home_batch_takein = validated_data.get('play_home_batch_takein', instance.play_home_batch_takein)
        instance.play_home_batch_start_time = validated_data.get('play_home_batch_start_time', instance.play_home_batch_start_time)
        instance.play_flexi_batch_start_time = validated_data.get('play_flexi_batch_start_time', instance.play_flexi_batch_start_time)
        instance.play_general_cut_off = validated_data.get('play_general_cut_off', instance.play_general_cut_off)
        instance.play_game_version = validated_data.get('play_game_version', instance.play_game_version)
        instance.play_game_rating = validated_data.get('play_game_rating', instance.play_game_rating)
        instance.play_enable_fixture = validated_data.get('play_enable_fixture', instance.play_enable_fixture)
        instance.play_fixture_reminder_sent = validated_data.get('play_fixture_reminder_sent', instance.play_fixture_reminder_sent)
        instance.play_assigned_buddy1 = validated_data.get('play_assigned_buddy1', instance.play_assigned_buddy1)
        instance.play_assigned_buddy2 = validated_data.get('play_assigned_buddy2', instance.play_assigned_buddy2)
        instance.play_temp_buddy1 = validated_data.get('play_temp_buddy1', instance.play_temp_buddy1)
        instance.play_temp_buddy2 = validated_data.get('play_temp_buddy2', instance.play_temp_buddy2)
        instance.play_session_description = validated_data.get('play_session_description', instance.play_session_description)
        instance.save()
        return instance


"""
Improve Game slot details serializer
"""


class Improve_game_slot_details_Serializer(serializers.Serializer):
   
    improve_fixture_id = serializers.IntegerField(required=True)
    improve_game_day = serializers.CharField(required=True, max_length=255)
    improve_venue_id = serializers.IntegerField(required=True)
    improve_game_slot = serializers.CharField( required=True, allow_blank=False, max_length=100)
    improve_court_name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    improve_game_max_players = serializers.IntegerField(required=True)
    improve_home_batch_takein = serializers.IntegerField(required=True)
    improve_home_batch_start_time = serializers.CharField(required=True, allow_blank=False, max_length=10)
    improve_flexi_batch_start_time = serializers.CharField(required=True, allow_blank=False, max_length=10)
    improve_general_cut_off = serializers.CharField(required=True, allow_blank=False, max_length=10)
    improve_game_version = serializers.CharField(required=True, allow_blank=False, max_length=5)
    improve_game_rating = serializers.CharField(required=True, allow_blank=False, max_length=15)
    improve_enable_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_fixture_reminder_sent = serializers.CharField(allow_blank=True, max_length=255)
    improve_flexi_fixture_reminder_sent = serializers.CharField(allow_blank=True, max_length=255)
    improve_no_buddy_required = serializers.IntegerField(required=True)
    improve_session_description = serializers.CharField(required=True, allow_blank=False, max_length=255)
 
 



    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Improve_game_slot_details.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.improve_fixture_id = validated_data.get('improve_fixture_id', instance.improve_fixture_id)
        instance.improve_game_day = validated_data.get('improve_game_day', instance.improve_game_day)
        instance.improve_venue_id = validated_data.get('improve_venue_id', instance.improve_venue_id)
        instance.improve_game_slot = validated_data.get('improve_game_slot', instance.improve_game_slot)
        instance.improve_court_name = validated_data.get('improve_court_name', instance.improve_court_name)
        instance.improve_game_max_players = validated_data.get('improve_game_max_players', instance.improve_game_max_players)
        instance.improve_home_batch_takein = validated_data.get('improve_home_batch_takein', instance.improve_home_batch_takein)
        instance.improve_home_batch_start_time = validated_data.get('improve_home_batch_start_time', instance.improve_home_batch_start_time)
        instance.improve_flexi_batch_start_time = validated_data.get('improve_flexi_batch_start_time', instance.improve_flexi_batch_start_time)
        instance.improve_general_cut_off = validated_data.get('improve_general_cut_off', instance.improve_general_cut_off)
        instance.improve_game_version = validated_data.get('improve_game_version', instance.improve_game_version)
        instance.improve_game_rating = validated_data.get('improve_game_rating', instance.improve_game_rating)
        instance.improve_enable_fixture = validated_data.get('improve_enable_fixture', instance.improve_enable_fixture)
        instance.improve_fixture_reminder_sent = validated_data.get('improve_fixture_reminder_sent', instance.improve_fixture_reminder_sent)
        instance.improve_assigned_buddy1 = validated_data.get('improve_assigned_buddy1', instance.improve_assigned_buddy1)
        instance.improve_assigned_buddy2 = validated_data.get('improve_assigned_buddy2', instance.improve_assigned_buddy2)
        instance.improve_temp_buddy1 = validated_data.get('improve_temp_buddy1', instance.improve_temp_buddy1)
        instance.improve_temp_buddy2 = validated_data.get('improve_temp_buddy2', instance.improve_temp_buddy2)
        instance.improve_session_description = validated_data.get('improve_session_description', instance.improve_session_description)
        instance.save()
        return instance
