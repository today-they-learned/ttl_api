from django.contrib import admin
from user.models import Grass


@admin.register(Grass)
class GrassAdmin(admin.ModelAdmin):
    """Admin View for Grass"""

    list_display = (
        "user",
        "study_count",
        "write_count",
        "edit_count",
        "created_at",
    )

    ordering = ("created_at",)
