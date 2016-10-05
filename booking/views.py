# coding=utf-8
from django.shortcuts import render

from rest_framework.permissions import IsAdminUser

# Create your views here.


from booking.serializers import LogSerializer,FootballPlayProgressSerializer,FootballImproveProgressSerializer

from booking.models import BookingLog,FootballPlayProgress,FootballImproveProgress

from customer.models import Customer,GameLevel

from gameinfo.models import Details

from rest_framework import serializers, viewsets, filters, generics






# ViewSets define the view behavior.
class BookingLogViewSet(viewsets.ModelViewSet):
    queryset = BookingLog.objects.all()
    serializer_class = LogSerializer



# ViewSets define the view behavior.
class FootballPlayProgressViewSet(viewsets.ModelViewSet):
    queryset = FootballPlayProgress.objects.raw('SELECT customer_customer.customerpic,customer_customer.id,customer_customer.firstname, booking_footballplayprogress.matchpoints FROM booking_footballplayprogress, customer_customer, booking_bookinglog, customer_gamelevel, gameinfo_position WHERE booking_footballplayprogress.id = booking_bookinglog.id AND booking_bookinglog.customer_id = customer_customer.id AND customer_customer.id = customer_gamelevel.customer_id AND customer_gamelevel.gameposition_id = gameinfo_position.id  AND gameinfo_position.gamedetails_id =1 ORDER BY booking_footballplayprogress.matchpoints DESC')
    serializer_class = FootballPlayProgressSerializer


# ViewSets define the view behavior.
class TopForwardViewSet(viewsets.ModelViewSet):
    queryset = FootballPlayProgress.objects.raw('SELECT customer_customer.customerpic,customer_customer.id,customer_customer.firstname, booking_footballplayprogress.matchpoints FROM booking_footballplayprogress, customer_customer, booking_bookinglog, customer_gamelevel, gameinfo_position WHERE booking_footballplayprogress.id = booking_bookinglog.id AND booking_bookinglog.customer_id = customer_customer.id AND customer_customer.id = customer_gamelevel.customer_id AND customer_gamelevel.gameposition_id = gameinfo_position.id  AND gameinfo_position.id =1 AND gameinfo_position.gamedetails_id =1 ORDER BY booking_footballplayprogress.matchpoints DESC')
    serializer_class = FootballPlayProgressSerializer

# ViewSets define the view behavior.
class TopDefenderViewSet(viewsets.ModelViewSet):
    queryset = FootballPlayProgress.objects.raw('SELECT customer_customer.customerpic,customer_customer.id,customer_customer.firstname, booking_footballplayprogress.matchpoints FROM booking_footballplayprogress, customer_customer, booking_bookinglog, customer_gamelevel, gameinfo_position WHERE booking_footballplayprogress.id = booking_bookinglog.id AND booking_bookinglog.customer_id = customer_customer.id AND customer_customer.id = customer_gamelevel.customer_id AND customer_gamelevel.gameposition_id = gameinfo_position.id  AND gameinfo_position.id =2 AND gameinfo_position.gamedetails_id =1 ORDER BY booking_footballplayprogress.matchpoints DESC')
    serializer_class = FootballPlayProgressSerializer


# ViewSets define the view behavior.
class TopMidfieldViewSet(viewsets.ModelViewSet):
    queryset = FootballPlayProgress.objects.raw('SELECT customer_customer.customerpic,customer_customer.id,customer_customer.firstname, booking_footballplayprogress.matchpoints FROM booking_footballplayprogress, customer_customer, booking_bookinglog, customer_gamelevel, gameinfo_position WHERE booking_footballplayprogress.id = booking_bookinglog.id AND booking_bookinglog.customer_id = customer_customer.id AND customer_customer.id = customer_gamelevel.customer_id AND customer_gamelevel.gameposition_id = gameinfo_position.id  AND gameinfo_position.id =4 AND gameinfo_position.gamedetails_id =1 ORDER BY booking_footballplayprogress.matchpoints DESC')
    serializer_class = FootballPlayProgressSerializer





# ViewSets define the view behavior.
class FootballImproveProgressViewSet(viewsets.ModelViewSet):
    queryset = FootballImproveProgress.objects.all()
    serializer_class = FootballImproveProgressSerializer



