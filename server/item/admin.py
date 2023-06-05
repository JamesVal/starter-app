from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Item Details",
            {"fields": ["itemName", "itemDescription", "owner"]},
        ),
    )
    list_display = (
        "id",
        "itemName",
        "itemDescription",
        "owner",
    )


admin.site.register(Item, ItemAdmin)
