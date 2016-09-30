

from django.contrib import admin

from .models import Customer,CustomerLog,Subscription,GamePreference,GameLevel

admin.site.register(Customer)
admin.site.register(CustomerLog)
admin.site.register(Subscription)
admin.site.register(GamePreference)
admin.site.register(GameLevel)