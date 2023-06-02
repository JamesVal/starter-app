from django.contrib import admin
from .models import Type

class TypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Type Details",
            {"fields": ["typeName", "typeDescription"]},
        ),
    )
    list_display = (
        "id",
        "typeName",
    )


admin.site.register(Type, TypeAdmin)
