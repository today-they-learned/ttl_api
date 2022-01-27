from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin View for User"""

    list_display = (
        "email",
        "username",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = (
        "email",
        "username",
    )
    ordering = (
        "created_at",
        "updated_at",
    )
