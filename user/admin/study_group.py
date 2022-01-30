from django.contrib import admin
from user.models import StudyGroup


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    """Admin View for StudyGroup"""

    list_display = (
        "name",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = ("name",)
    ordering = (
        "created_at",
        "updated_at",
    )
