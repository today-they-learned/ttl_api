from django.contrib import admin
from study.models import Study


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    """Admin View for Study"""

    list_display = (
        "user",
        "article",
        "studied_at",
    )
    readonly_fields = ("studied_at",)
    ordering = ("studied_at",)
