from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

class IdentiteCompleteAdmin(admin.ModelAdmin):
    list_display = ('attestionId', 'date')
    list_filter = ('slug', )


admin.site.register(IdentiteComplete, IdentiteCompleteAdmin)
admin.site.unregister(Group)
admin.site.site_header = "RIHA"