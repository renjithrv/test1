

from django.contrib import admin

from .models import Customer,CustomerLog,GamePreference,GameLevel

admin.site.register(Customer)
admin.site.register(CustomerLog)
admin.site.register(GamePreference)
admin.site.register(GameLevel)