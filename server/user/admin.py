from django.contrib import admin
from .models import User, Account

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "User Details",
            {"fields": ["email"]},
        ),
    )
    list_display = (
        "id",
        "is_active",
        "email",
    )

class AccountAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Account Details",
            {"fields": ["user", "accountName", "type"]},
        ),
    )
    list_display = (
        "id",
        "accountName",
        "type",
        "user",
    )


admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)


