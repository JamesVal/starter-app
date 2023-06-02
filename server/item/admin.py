from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Type Details",
            {"fields": ["itemName", "itemDescription"]},
        ),
    )
    list_display = (
        "id",
        "itemName",
        "itemDescription",
    )


admin.site.register(Item, ItemAdmin)