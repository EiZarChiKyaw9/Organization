from django.contrib import admin
from .models import list, Work_Volume, Slab_Level, WV_Main, WV_Daily_Report_Details, Site

admin.site.register(list)
admin.site.register(Work_Volume)
admin.site.register(Slab_Level)
admin.site.register(WV_Main)
admin.site.register(WV_Daily_Report_Details)
admin.site.register(Site)