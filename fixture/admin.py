

from django.contrib import admin

from .models import Fixture,BuddyAudit,AssignedBuddy,AssignedBuddyLog

admin.site.register(Fixture)
admin.site.register(BuddyAudit)
admin.site.register(AssignedBuddy)
admin.site.register(AssignedBuddyLog)