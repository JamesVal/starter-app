from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Comment Details",
            {"fields": ["content", "item", "owner"]},
        ),
    )
    list_display = (
        "id",
        "content",
        "item",
        "owner"
    )


admin.site.register(Comment, CommentAdmin)
