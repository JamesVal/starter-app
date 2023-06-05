from django.contrib import admin
from .models import User, Account, UserSelectedAccount

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

class UserSelectedAccountAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Selected Account Details",
            {"fields": ["user", "selected_account"]},
        ),
    )
    list_display = (
        "id",
        "user",
        "selected_account",
    )



admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(UserSelectedAccount, UserSelectedAccountAdmin)