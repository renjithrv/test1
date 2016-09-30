

from django.contrib import admin

from .models import Role,Buddy,BuddyRating

admin.site.register(Role)
admin.site.register(Buddy)
admin.site.register(BuddyRating)