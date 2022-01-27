from django.contrib import admin
from user.models import UserStudyGroup


@admin.register(UserStudyGroup)
class UserStudyGroupAdmin(admin.ModelAdmin):
    """Admin View for UserStudyGroup"""

    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = (
        "created_at",
        "updated_at",
    )
