"""sapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include 
from django.contrib import admin

from area.views import AreaViewSet
from booking.views import BookingLogViewSet,FootballPlayProgressViewSet,FootballImproveProgressViewSet
from buddy.views import BuddyViewSet,RoleViewSet,BuddyRatingViewSet
from customer.views import CustomerViewSet,CustomerLogViewSet,GamePreferenceViewSet,SubscriptionViewSet,GameLevelViewSet
from fixture.views import FixtureViewSet,BuddyAuditViewSet,AssignedBuddyViewSet,AssignedBuddyLogViewSet
from gameinfo.views import DetailsViewSet,TypeViewSet,LevelViewSet,DayViewSet
from package.views import PackageViewSet
from venue.views import VenueDetailsViewSet,VenueGamesAvailableViewSet


from rest_framework import routers





# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()

#Area Router
router.register(r'area', AreaViewSet)


#Booking Router

router.register(r'log', BookingLogViewSet)
router.register(r'footballplay', FootballPlayProgressViewSet)
router.register(r'footballimprove', FootballImproveProgressViewSet)


#Buddy Router

router.register(r'buddy', BuddyViewSet)
router.register(r'role', RoleViewSet)
router.register(r'buddyrating', BuddyRatingViewSet)



#Customer Router

router.register(r'customer', CustomerViewSet)
router.register(r'customerlog', CustomerLogViewSet)
router.register(r'customerpreference', GamePreferenceViewSet)
router.register(r'customersubscription', SubscriptionViewSet)
router.register(r'customergamelevel', GameLevelViewSet)



#Fixture Router


router.register(r'fixture', FixtureViewSet)
router.register(r'buddyaudit', BuddyAuditViewSet)
router.register(r'assignedbuddy', AssignedBuddyViewSet)
router.register(r'assignedbuddylog', AssignedBuddyLogViewSet)


#Gameinfo Router

router.register(r'gamedetails', DetailsViewSet)
router.register(r'gametype', TypeViewSet)
router.register(r'gamelevel', LevelViewSet)
router.register(r'gameday', DayViewSet)


#Package Router

router.register(r'package', PackageViewSet)

#Venue Router

router.register(r'venue', VenueDetailsViewSet)
router.register(r'venuegames', VenueGamesAvailableViewSet)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
