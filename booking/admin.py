

from django.contrib import admin

from .models import BookingLog,FootballImproveProgress,FootballPlayProgress

admin.site.register(BookingLog)
admin.site.register(FootballImproveProgress)
admin.site.register(FootballPlayProgress)