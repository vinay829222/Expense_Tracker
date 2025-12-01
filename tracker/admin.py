from django.contrib import admin
from tracker.models import *

admin.site.site_header="Expence Tracker"

admin.site.site_title="Expence Tracker"

admin.site.site_url="Expence Tracker"

# Register your models here.
admin.site.register(CurrentBalance)

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display=[
        "current_balance",
        "amount",
        "description",
        "expence_type",
        "created_at",
        "display"

    ]
    def display(self,obj):
        if obj.amount > 0:
            return "Positive"
        return "Negative"

    search_fields=['expence_type'] #create a searching tag and search item based on passages element
    ordering=['-created_at'] # for order 
    list_filter=["expence_type"]
admin.site.register(TrackingHistory,TrackingHistoryAdmin)


