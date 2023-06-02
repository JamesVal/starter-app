from django.contrib import admin
from .models import Type, TypeCategory

class TypeCategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Type Category Details",
            {"fields": ["categoryName", "categoryDescription"]},
        ),
    )
    list_display = (
        "id",
        "categoryName",
    )

class TypeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Type Details",
            {"fields": ["typeName", "typeDescription", "category"]},
        ),
    )
    list_display = (
        "id",
        "typeName",
        "category",
    )


admin.site.register(Type, TypeAdmin)
admin.site.register(TypeCategory, TypeCategoryAdmin)
