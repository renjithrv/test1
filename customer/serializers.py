from rest_framework import serializers
from customer.models import Play_customer_profile,Improve_customer_profile,Initial_customer_profile

"""
Play Customer Profile
"""


class Play_customer_Serializer(serializers.Serializer):

    play_customer_name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    play_customer_email = serializers.EmailField(required=True)
    play_mobile_number = serializers.IntegerField(required=True)
    play_amount_paid = serializers.CharField( required=True, allow_blank=False, max_length=100)
    play_membership_start_date = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_membership_end_date = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_preferred_monday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    play_monday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_preferred_tuesday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    wq = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_preferred_wednesday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    play_wednesday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_preferred_thursday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    play_thursday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_preferred_friday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    play_friday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_preferred_saturday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    play_saturday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_preferred_sunday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    play_sunday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    play_preferred_position = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_self_rating = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_number_games_left = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_flexi_flag = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_batch_type = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_preferred_venue = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_about_me = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_customer_picture = serializers.CharField(required=True, allow_blank=False, max_length=100)






    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Play_customer_profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.play_customer_name = validated_data.get('play_customer_name', instance.play_customer_name)
        instance.play_customer_email = validated_data.get('play_customer_email', instance.play_customer_email)
        instance.play_mobile_number = validated_data.get('play_mobile_number', instance.play_mobile_number)
        instance.play_amount_paid = validated_data.get('play_amount_paid', instance.play_amount_paid)
        instance.play_membership_start_date = validated_data.get('play_membership_start_date', instance.play_membership_start_date)
        instance.play_membership_end_date = validated_data.get('play_membership_end_date', instance.play_membership_end_date)
        instance.play_preferred_monday = validated_data.get('play_preferred_monday', instance.play_preferred_monday)
        instance.play_monday_fixture = validated_data.get('play_monday_fixture', instance.play_monday_fixture)
        instance.play_preferred_tuesday = validated_data.get('play_preferred_tuesday', instance.play_preferred_tuesday)
        instance.play_tuesday_fixture = validated_data.get('play_tuesday_fixture', instance.play_tuesday_fixture)
        instance.play_preferred_wednesday = validated_data.get('play_preferred_wednesday', instance.play_preferred_wednesday)
        instance.play_wednesday_fixture = validated_data.get('play_wednesday_fixture', instance.play_wednesday_fixture)
        instance.play_preferred_thursday = validated_data.get('play_preferred_thursday', instance.play_preferred_thursday)
        instance.play_thursday_fixture = validated_data.get('play_thursday_fixture', instance.play_thursday_fixture)
        instance.play_preferred_friday = validated_data.get('flexiflag', instance.play_preferred_friday)
        instance.play_friday_fixture = validated_data.get('play_friday_fixture', instance.play_friday_fixture)
        instance.play_preferred_saturday = validated_data.get('play_preferred_saturday', instance.play_preferred_saturday)
        instance.play_saturday_fixture = validated_data.get('play_saturday_fixture', instance.play_saturday_fixture)
        instance.play_preferred_sunday = validated_data.get('play_preferred_sunday', instance.play_preferred_sunday)
        instance.play_sunday_fixture = validated_data.get('play_sunday_fixture', instance.play_sunday_fixture)
        instance.play_preferred_position = validated_data.get('play_preferred_position', instance.play_preferred_position)
        instance.play_self_rating = validated_data.get('play_self_rating', instance.play_self_rating)
        instance.play_number_games_left = validated_data.get('play_number_games_left', instance.play_number_games_left)
        instance.play_flexi_flag = validated_data.get('play_flexi_flag', instance.play_flexi_flag)
        instance.play_batch_type = validated_data.get('play_batch_type', instance.play_batch_type)
        instance.play_preferred_venue = validated_data.get('play_preferred_venue', instance.play_preferred_venue)
        instance.play_about_me = validated_data.get('play_about_me', instance.play_about_me)
        instance.play_customer_picture = validated_data.get('play_customer_picture', instance.play_customer_picture)
        instance.save()
        return instance


"""
Improve Customer Profile
"""



class Improve_customer_Serializer(serializers.Serializer):
    improve_customer_name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    improve_customer_email = serializers.EmailField(required=True)
    improve_mobile_number = serializers.IntegerField(required=True)
    improve_amount_paid = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_membership_start_date = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_membership_end_date = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_preferred_monday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    improve_monday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_preferred_tuesday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    improve_tuesday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_preferred_wednesday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    improve_wednesday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_preferred_thursday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    improve_thursday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_preferred_friday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    improve_friday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_preferred_saturday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    improve_saturday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_preferred_sunday = serializers.CharField(required=True, allow_blank=False, max_length=1)
    improve_sunday_fixture = serializers.CharField(required=True, allow_blank=False, max_length=4)
    improve_preferred_position = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_self_rating = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_number_games_left = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_flexi_flag = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_batch_type = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_preferred_venue = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_about_me = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_customer_picture = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return improve_customer_profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.improve_customer_name = validated_data.get('improve_customer_name', instance.improve_customer_name)
        instance.improve_customer_email = validated_data.get('improve_customer_email', instance.improve_customer_email)
        instance.improve_mobile_number = validated_data.get('improve_mobile_number', instance.improve_mobile_number)
        instance.improve_amount_paid = validated_data.get('improve_amount_paid', instance.improve_amount_paid)
        instance.improve_membership_start_date = validated_data.get('improve_membership_start_date',
                                                                    instance.improve_membership_start_date)
        instance.improve_membership_end_date = validated_data.get('improve_membership_end_date',
                                                                  instance.improve_membership_end_date)
        instance.improve_preferred_monday = validated_data.get('improve_preferred_monday',
                                                               instance.improve_preferred_monday)
        instance.improve_monday_fixture = validated_data.get('improve_monday_fixture', instance.improve_monday_fixture)
        instance.improve_preferred_tuesday = validated_data.get('improve_preferred_tuesday',
                                                                instance.improve_preferred_tuesday)
        instance.improve_tuesday_fixture = validated_data.get('improve_tuesday_fixture',
                                                              instance.improve_tuesday_fixture)
        instance.improve_preferred_wednesday = validated_data.get('improve_preferred_wednesday',
                                                                  instance.improve_preferred_wednesday)
        instance.improve_wednesday_fixture = validated_data.get('improve_wednesday_fixture',
                                                                instance.improve_wednesday_fixture)
        instance.improve_preferred_thursday = validated_data.get('improve_preferred_thursday',
                                                                 instance.improve_preferred_thursday)
        instance.improve_thursday_fixture = validated_data.get('improve_thursday_fixture',
                                                               instance.improve_thursday_fixture)
        instance.improve_preferred_friday = validated_data.get('flexiflag', instance.improve_preferred_friday)
        instance.improve_friday_fixture = validated_data.get('improve_friday_fixture', instance.improve_friday_fixture)
        instance.improve_preferred_saturday = validated_data.get('improve_preferred_saturday',
                                                                 instance.improve_preferred_saturday)
        instance.improve_saturday_fixture = validated_data.get('improve_saturday_fixture',
                                                               instance.improve_saturday_fixture)
        instance.improve_preferred_sunday = validated_data.get('improve_preferred_sunday',
                                                               instance.improve_preferred_sunday)
        instance.improve_sunday_fixture = validated_data.get('improve_sunday_fixture', instance.improve_sunday_fixture)
        instance.improve_preferred_position = validated_data.get('improve_preferred_position',
                                                                 instance.improve_preferred_position)
        instance.improve_self_rating = validated_data.get('improve_self_rating', instance.improve_self_rating)
        instance.improve_number_games_left = validated_data.get('improve_number_games_left',
                                                                instance.improve_number_games_left)
        instance.improve_flexi_flag = validated_data.get('improve_flexi_flag', instance.improve_flexi_flag)
        instance.improve_batch_type = validated_data.get('improve_batch_type', instance.improve_batch_type)
        instance.improve_preferred_venue = validated_data.get('improve_preferred_venue',
                                                              instance.improve_preferred_venue)
        instance.improve_about_me = validated_data.get('improve_about_me', instance.improve_about_me)
        instance.improve_customer_picture = validated_data.get('improve_customer_picture',
                                                               instance.improve_customer_picture)
        instance.save()
        return instance



"""
Initial Customer Profile
"""

class Initial_customer_Serializer(serializers.Serializer):
    customer_username = serializers.CharField(required=True, allow_blank=True, max_length=100)
    customer_email = serializers.EmailField(required=True)
    customer_password = serializers.CharField(required=True)
    customer_mobile_number = serializers.CharField(required=True, allow_blank=False, max_length=100)
    play_customer_id = serializers.CharField(required=True, allow_blank=False, max_length=100)
    improve_customer_id = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Initial_customer_profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.customer_username = validated_data.get('customer_username', instance.customer_username)
        instance.customer_email = validated_data.get('customer_email', instance.customer_email)
        instance.customer_password = validated_data.get('customer_password', instance.customer_password)
        instance.customer_mobile_number = validated_data.get('customer_mobile_number', instance.customer_mobile_number)
        instance.play_customer_id = validated_data.get('play_customer_id', instance.play_customer_id)
        instance.improve_customer_id = validated_data.get('improve_customer_id', instance.improve_customer_id)

        instance.save()
        return instance