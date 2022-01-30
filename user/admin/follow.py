from django.contrib import admin
from user.models import Follow


@admin.register(Follow)
class UserAdmin(admin.ModelAdmin):
    """Admin View for Follow"""

    list_display = (
        "follower",
        "following",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = (
        "follower",
        "following",
    )
    ordering = (
        "created_at",
        "updated_at",
    )
