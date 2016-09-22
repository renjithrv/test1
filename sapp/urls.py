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
from customer.serializers import Play_customer_Serializer,Improve_customer_Serializer,Initial_customer_Serializer
from customer.models import Play_customer_profile,Improve_customer_profile,Initial_customer_profile

from rest_framework import routers, serializers, viewsets




# ViewSets define the view behavior.
class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play_customer_profile.objects.all()
    serializer_class = Play_customer_Serializer

    # ViewSets define the view behavior.
class ImproveViewSet(viewsets.ModelViewSet):
    queryset = Improve_customer_profile.objects.all()
    serializer_class = Improve_customer_Serializer


    # ViewSets define the view behavior.
class InitialViewSet(viewsets.ModelViewSet):
    queryset = Initial_customer_profile.objects.all()
    serializer_class = Initial_customer_Serializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'playcustomer', PlayViewSet)

router.register(r'improvecustomer', ImproveViewSet)

router.register(r'initialcustomer', InitialViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]