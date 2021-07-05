from django.contrib import admin

from .models import Tracker, Entry, Failure

admin.site.register(Tracker)
admin.site.register(Entry)
admin.site.register(Failure)
