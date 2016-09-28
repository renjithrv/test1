from django.conf.urls import url
from fixture.views import PlaygameslotViewSet

urlpatterns = [
    url(r'^playgameslotdetails/$', PlaygameslotViewSet, name='playgameslotdetails'),
    
]